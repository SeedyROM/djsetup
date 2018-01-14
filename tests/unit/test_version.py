from djsetup.version import Version
from tests import *
from tests.helpers import *


class TestVersion(unittest.TestCase):

    def test_set_version(self):
        ver = Version("0.0.1")
        self.assertEqual(ver.number, "0.0.1")

    def test_version_immutable(self):
        ver = Version("0.0.1")
        with pytest.raises(TypeError) as e:
            ver.number = "0.0.2"
