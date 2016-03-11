"""This tests git_utils"""
from unittest import TestCase
from mock import mock
from source.main import Interface
from source.git_utils import is_file_in_repo, os, has_untracked_files,\
    get_git_file_info, get_repo_root
from test.plugins.ReqTracer import requirements



class TestMock(TestCase):
    """This tests mocking"""

    @requirements({"#0100"})
    @mock.patch('subprocess.Popen')
    def test_mock_file_in_repo(self, mock_subproc_popen):
        """This tests mocking a file in the repo"""
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('true', 'File not found')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        inquiry = Interface()
        result = inquiry.ask("Is the <nose2.cfg> in the repo?")
        self.assertEqual(result, "Yes")

    @requirements({"#0100"})
    @mock.patch('subprocess.Popen')
    def test_repo_dirty(self, mock_subproc_popen):
        """This tests if the po is dirty"""
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('true', 'Repo not dirty')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        inquiry = Interface()
        result = inquiry.ask("Is the <> in the repo?")
        self.assertEqual(result, "No")

    @requirements({"#0100"})
    @mock.patch('source.git_utils.get_diff_files')
    def test_file_untracked(self, mock_diff_files):
        """This tests if the file is untracked"""
        blah = 'requirements.txt'
        mock_diff_files.return_value = os.path.abspath(blah)
        result = is_file_in_repo(blah)
        self.assertEqual(result, 'No')

    @requirements({"#0101"})
    @mock.patch('subprocess.Popen')
    def test_up_to_date(self, mock_subproc_popen):
        """This tests if a file is up to date"""
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        inquiry = Interface()
        result = inquiry.ask("What is the status of <nose2.cfg>?")
        self.assertEqual(result, "nose2.cfg is up to date")

    @requirements({"#0101"})
    @mock.patch('subprocess.Popen')
    def test_dirty_repo(self, mock_subproc_popen):
        """This tests if the repo is dirty"""
        process_mock = mock.Mock()
        attrs = {'communicate.side_effect': [('', ''),
                                             ('', ''),
                                             ('', ''),
                                             ('', ''),
                                             ('dirty', ''),
                                             ('', '')]}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        inquiry = Interface()
        result = inquiry.ask("What is the status of <nose2.cfg>?")
        self.assertEqual(result, "nose2.cfg is a dirty repo")

    @requirements({"#0101"})
    @mock.patch('source.git_utils.get_untracked_files')
    def test_untracked_files(self, mock_get_untracked_files):
        """This test if there are untracked files"""
        mock_get_untracked_files.return_value = 'fuck_this'
        result = has_untracked_files('requirements.txt')
        self.assertEqual(result, True)

    @requirements({"#0101"})
    @mock.patch('source.git_utils.get_diff_files')
    def test_file_diff(self, mock_diff_files):
        """This tests if a file has been modified locally"""
        blah = 'requirements.txt'
        mock_diff_files.return_value = os.path.abspath(blah)
        result = get_git_file_info(blah)
        self.assertEqual(result, 'requirements.txt has been modified locally')

    @requirements({"#0101"})
    @mock.patch('source.git_utils.get_untracked_files')
    @mock.patch('source.git_utils.get_diff_files')
    def test_file_untracked_for_ggfi(self, mock_diff_files, mock_untracked_files):
        """This tests if a file has been checked in"""
        blah = 'requirements.txt'
        mock_diff_files.return_value = ''
        mock_untracked_files.return_value = os.path.abspath(blah)
        result = get_git_file_info(blah)
        self.assertEqual(result, 'requirements.txt has been not been checked in')

    @requirements({"#0101"})
    @mock.patch('source.git_utils.git_execute')
    def test_repo_root(self, mock_repo_root):
        """This tests the repo root"""
        blah = os.path.abspath('requirements.txt')
        mock_repo_root.return_value = blah
        result = get_repo_root(blah)
        self.assertEqual(result, blah)

    @requirements({"#0102"})
    @mock.patch('subprocess.Popen')
    def test_file_info(self, mock_subproc_popen):
        """This tests the file info"""
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('352364, 10:42:15 02/27/2016, Keyul Patel', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        inquiry = Interface()
        result = inquiry.ask("What is the deal with <nose2.cfg>?")
        self.assertEqual(result, "352364, 10:42:15 02/27/2016, Keyul Patel")

    @requirements({"#0103"})
    @mock.patch('subprocess.Popen')
    def test_repo_branch(self, mock_subproc_popen):
        """This tests the repo branch"""
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('Lab 5', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        inquiry = Interface()
        result = inquiry.ask("What branch is <nose2.cfg>?")
        self.assertEqual(result, "Lab 5")

    @requirements({"#0104"})
    @mock.patch('subprocess.Popen')
    def test_repo_url(self, mock_subproc_popen):
        """This tests the repo url"""
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('git, config, '
                                              '--get, https://github.com'
                                              '/OregonTech/KeyulP.git', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        inquiry = Interface()
        result = inquiry.ask("Where did <requirements.txt> come from?")
        self.assertEqual(result, 'git, config, --get, https://github.com/OregonTech/KeyulP.git')

    @requirements({"#0104"})
    @mock.patch('subprocess.Popen')
    def test_repo_false_url(self, mock_subproc_popen):
        """This tests a bad repo url"""
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('', 'git_logger.error')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        inquiry = Interface()
        result = inquiry.ask("Where did <requirements.txt> come from?")
        self.assertEqual(result, '')

    @requirements({"#0105"})
    @mock.patch('subprocess.Popen')
    def test_exception_wrong_file_path(self, mock_subproc_popen):
        """This tests the exception for the wrong file path"""
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        with self.assertRaises(Exception, msg="Path blah.txt does not exist cannot get git file"):
            inquiry = Interface()
            result = inquiry.ask("What is the deal with <blah.txt>?")
            self.assertEqual(result, '')
