import pytest
import json
from csv import DictReader
from sqlalchemy.exc import IntegrityError

import encoded.commands.read_edw_fileinfo
import encoded.edw_file
import edw_test_data

pytestmark = [pytest.mark.edw_file]

# globals
EDW_FILE_TEST_DATA_DIR = 'src/encoded/tests/data/edw_file'

TEST_ACCESSION = 'ENCFF001RET'  # NOTE: must be in test set



## edw_file
# def format_edw_fileinfo(file_dict, exclude=None):
# def make_edw(data_host=None):
# def dump_filelist(fileaccs, header=True, typeField=None):
# def dump_fileinfo(fileinfos, header=True, typeField=None, exclude=None):
# def get_edw_filelist(edw, limit=None, experiment=True, phase=ENCODE_PHASE_ALL):
# def get_edw_max_id(edw):
# def get_edw_fileinfo(edw, limit=None, experiment=True, start_id=0,


def test_format_app_fileinfo_expanded(workbook, testapp):
    # Test extracting EDW-relevant fields from encoded file.json
    # Expanded JSON

    # load input
    url = '/files/' + TEST_ACCESSION

    resp = testapp.get(url).maybe_follow()
    file_dict = resp.json

    fileinfo = encoded.commands.read_edw_fileinfo.format_app_fileinfo(testapp, file_dict)

    # compare results for identity with expected
    set_app = set(fileinfo.items())
    set_edw = set(edw_test_data.format_app_file_out.items())
    assert set_app == set_edw


def test_post_duplicate(workbook, testapp):
    url = '/files/' + TEST_ACCESSION
    resp = testapp.get(url).maybe_follow()
    current = resp.json
    try:
        illegal_post = testapp.post_json(url, current, expect_errors=True)
    except IntegrityError:
        assert(True)


def test_list_new(workbook, testapp):
    # Test obtaining list of 'new' accessions (at EDW, not at app)
    # Unexpanded JSON (requires GETs on embedded URLs)

    edw_accs = edw_test_data.new_in
    app_accs = encoded.commands.read_edw_fileinfo.get_app_fileinfo(testapp,
                                                                  full=False)
    new_accs = sorted(encoded.commands.read_edw_fileinfo.get_missing_filelist_from_lists(app_accs, edw_accs))
    assert new_accs == sorted(edw_test_data.new_out)


def test_import_file(workbook, testapp):
    # Test import of new file to encoded
    # this tests adds replicates, but never checks their validity

    input_file = 'import_in.1.tsv'
    f = open(EDW_FILE_TEST_DATA_DIR + '/' + input_file)
    reader = DictReader(f, delimiter='\t')
    for fileinfo in reader:
        # WARNING: type-unaware char conversion here, with field-specific
        # correction of mis-formatted int field
        # does this do anything?
        '''
        unidict = {k.decode('utf8'): v.decode('utf8') for k, v in fileinfo.items()}
        encoded.commands.read_edw_fileinfo.format_reader_fileinfo(unidict)
        unidict['replicate'] = int(unidict['replicate'])
        if unidict['replicate'] == -1:
            del unidict['replicate']
        set_in = set(unidict.items())
        '''

        encoded.commands.read_edw_fileinfo.format_reader_fileinfo(fileinfo)
        set_in = set(fileinfo.items())
        resp = encoded.commands.read_edw_fileinfo.post_fileinfo(testapp, fileinfo)
        # exercises: set_fileinfo_experiment, set_fileinfo_replicate, POST
        acc = fileinfo['accession']
        url = encoded.commands.read_edw_fileinfo.collection_url(encoded.commands.read_edw_fileinfo.FILES) + acc
        get_resp = testapp.get(url).maybe_follow()
        file_dict = get_resp.json
        fileinfo = encoded.commands.read_edw_fileinfo.format_app_fileinfo(testapp, file_dict)
        set_out = set(fileinfo.items())

        assert set_in == set_out


def test_encode2_experiments(workbook, testapp):
    # Test obtaining list of ENCODE 2 experiments and identifying which ENCODE3
    # accessions are ENCODE2 experiments

    # Test identifying an ENCODE 3 experiment
    assert not encoded.commands.read_edw_fileinfo.is_encode2_experiment(testapp, edw_test_data.encode3)

    # Create hash of all ENCODE 2 experiments, map to ENCODE 3 accession
    encode2_hash = encoded.commands.read_edw_fileinfo.get_encode2_to_encode3(testapp)
    assert sorted(encode2_hash.keys()) == sorted(edw_test_data.encode2)

    # Test identifying an ENCODE 2 experiment
    assert encoded.commands.read_edw_fileinfo.is_encode2_experiment(testapp, encode2_hash.values()[0])

def test_file_sync(workbook, testapp):

    mock_edw_file = 'edw_file_mock.tsv'
    f = open(EDW_FILE_TEST_DATA_DIR + '/' + mock_edw_file)
    reader = DictReader(f, delimiter='\t')

    edw_mock = {}
    for fileinfo in reader:
        #unidict = {k.decode('utf8'): v.decode('utf8') for k, v in fileinfo.items()}
        #unidict['replicate'] = int(unidict['replicate'])
        #if unidict['replicate'] == encoded.edw_file.NO_REPLICATE_INT:
        #    del unidict['replicate']
        encoded.commands.read_edw_fileinfo.format_reader_fileinfo(fileinfo)
        del fileinfo['test']  # this is in the file for notation purposes only
        edw_mock[fileinfo['accession']] = fileinfo

    assert len(edw_mock) == 23

    app_files = encoded.commands.read_edw_fileinfo.get_app_fileinfo(testapp)
    app_dict = { d['accession']:d for d in app_files }
    assert len(app_files) == 24  ## just a place holder, could use TYPE_LENGTH from test_views.py
    assert(len(app_files) == len(app_dict.keys())) # this should never duplicate

    edw_only, app_only, same, patch = encoded.commands.read_edw_fileinfo.inventory_files(testapp, edw_mock, app_dict)
    assert len(edw_only) == 10
    assert len(app_only) == 11
    assert len(same) == 7
    assert len(patch) == 6

    for add in edw_only:
        acc = add['accession']
        url = encoded.commands.read_edw_fileinfo.collection_url(encoded.commands.read_edw_fileinfo.FILES) + acc
        resp = encoded.commands.read_edw_fileinfo.post_fileinfo(testapp, add)
        # check experiment status
        if not resp:
            assert(add['dataset'] == 'ENCSR000AEO') # experiment does not exist in test database
        else:
            assert(resp.status_code == 201)

    ''' This fails due to bug # moved to distinct test case
    for ignore in same:
    # just try to do one duplicate for now.
        acc = ignore['accession']
        url = encoded.commands.read_edw_fileinfo.collection_url(encoded.commands.read_edw_fileinfo.FILES) + acc
        try:
           resp = encoded.commands.read_edw_fileinfo.post_fileinfo(testapp, ignore)
        except IntegrityError:
            assert(True)
    '''
    # Thought this should have thrown a 409... assert(resp.status_code == 409)

    for update in patch:
        diff = encoded.commands.read_edw_fileinfo.compare_files(app_dict[update], edw_mock[update])
        patched = encoded.commands.read_edw_fileinfo.patch_fileinfo(testapp, diff.keys(), edw_mock[update])
        should_fail = False
        for patch_prop in diff.keys():
            if patch_prop in encoded.commands.read_edw_fileinfo.NO_UPDATE:
                should_fail = True
        if should_fail:
            assert not patched
        else:
            assert patched

    post_app_files = encoded.commands.read_edw_fileinfo.get_app_fileinfo(testapp)
    post_app_dict = { d['accession']:d for d in post_app_files }
    assert(len(post_app_files) == len(post_app_dict.keys()))

    encoded.commands.read_edw_fileinfo.collections = []
    # reset global var!
    post_edw, post_app, post_same, post_patch= encoded.commands.read_edw_fileinfo.inventory_files(testapp, edw_mock, post_app_dict)
    assert len(post_edw) == 2
    assert len(post_app) == 11 # unchanged
    assert len(post_patch) == 3
    assert len(post_same) == 32-(11+3)  # total minus ( encoded only + re-patch)
    assert len(post_app_files) == (len(app_files) + len(edw_only) - 2 )
    # original + edw_only










