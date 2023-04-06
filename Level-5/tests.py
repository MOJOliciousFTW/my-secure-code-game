import unittest
import code as c


class TestCrypto(unittest.TestCase):
    # verifies that hash and verification are matching each other for argon
    def test_0(self):
        argon = c.Argon2Hasher()
        pass_ver = argon.check_password("abc", argon.get_initial_hash("abc"))
        self.assertEqual(pass_ver, True)


if __name__ == "__main__":
    unittest.main()
