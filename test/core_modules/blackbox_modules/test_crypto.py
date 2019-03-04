import unittest

from core_modules.blackbox_modules.crypto import get_Ed521


class TestCrypto(unittest.TestCase):
    def setUp(self):
        self.data = b'TEST DATA'
        self.privkey = b'G\xba\xd9%%\xe3\x93\xffj{\x96Q\x9a\xab#\xbe\xd79\x92\xa4\x99yl>\\lZT\x88\x89\x86D.\xfb\xc2[\xdcD\xb5\xdf\x9d\xc8\x8d\xc1f\\\xc3\x9ei\xf0\xa9\xeb^|\x841\xbf\xa8`9\x7f0\xd5\xe9B\x10\x13e\xcf_\xf4\x8d\xb1\xbb\xdd\xf5K\xfd\xd2E:\xad\xf9\tNt\x88\x0f\xd5k\xce\xe0\x9c\xf3\x915\xde\xab\xd6\x14\xe0\xb2n\x9d\xd5\xc7\x9f\xd8%p\xac\x97\xec\xaf\xc6\xcckL\x19}-Z0\xbf^\x8dj\xa9\x0b\x98\xb3#\xa1\x99s/\xc7\x83S\x84\x0b\x16#\x1d\x0ca9=j\xddN\xa4u\x1cCW`G\xefL\xd1\r\xb5 \xf3\xb9\xd7\xbe\xe4-Ek\x15\xc6\x1f\xb9\xdbb\xf7\x1fN*D\xce_\x08\xed\xd8\xe5npF\x12\x89\xc9\x91\x9a^\xa7\x8c$\xd2\xc2\xd1\x00Hk\xec\x0eTO\xe3\x83\x04V\x89\xc7}\t\x929J4h\xb9I"\x1f\x05\xbb6Y\xd7, \xf9\xee\xc5U8\x153tHo\xc0\xf7\xf0\x1bH\xc5\xb2\xe3Ua\xc6\x14q\x98i\x16\xdaD\x1e\x9c\x0cU\x84\xbap\x01\t\x05gWQw\xa4\x91\x9b\t\x16\x078\x14,\xd4\xe4`\x86\xa3\xc6\xaa:\xbdG\\\xb1(s\x90\xf8\xf9\x8e\xe7T\x04j3\x1e\xa5\x1a\xc8\xea\xff\xf7m?w\xb1\x8c\x1bw\x08[\x99J!\x91\x9f\xe7\xbb\xb2\xfeXxXi=\x89 \x83E\xbfj:\x1c\xce\x19\xd0\x13j\xee\xc4\xee"/\xd3\xd5\xf6\xe3\xf3@{\xa0\xb3\xfe\xe2\x01\x84v\x8f\xb4\xbev\xe6\x05\xe1\xb3\xf8\xf6\xad{\xef\xa6\xd9\x80xv \x1e\xc6\xed\xc2\x8fK\xe5\xf0\xae\xcf\xd6O\xa8\xcd\xc3\xbc,\xcb\xf6\xee\xb6e\x8c\xf1\x8c\x9f\xf8.\x03v\xb8~\xe99g\xee\x89cO\x04\xb7l\x11\xb3h\xf6ear2\xfaq(\x14\xf6\xc6Q\x0bsd\xc0\xf2\x928y\xa9u\xea\x0b\xa4?3f\xaa\x14\xd3C\xea9\xaa\xea\x90\x0e\x887\xben\xa6T\xa8pDa:\x8dtF\x17\x87\xa0m\xa2\xea1\x85\xf9\xc6\x8d\xf2\x1a\x96l\x1f\x18K\x81S\xfc\xa7\xdb\xd9\xa5\x88,\x0c5#\tc\x927HA\x81G\x82\xe7W\x0e\xdcS\x8e\xa24%\xe9\xa1\xf8\xd6 \xaf\xa8\x10\x02\x88\x0eL\xfd\x86^\xe6\xb4-nAc\xaf=\x97\xe8\xf9\x06\x9f\xef\xf0z\xae\x87)\xaa\x98\x8c\xed\xf6\xbc\x84\x1d\x0e\xc1Zn%\xd7\x07o\x02\x14\x1e\x97\xa2 \x10\xce\x95\xca\x87\xc0\t\xe3\xd3MQ\xa5[ y\xce\xb6\x10\xd5\xfc_Sc\x18\x8bT\x14\xd4\x82*\xa9\x8f\x87\xe7:\xb6\xb6\x86\x91)\x1d\xf3\'\x067\x91\xe2\x87\xf4z\x92\xf7J\xabj\xda\xce\xf70\x02`p\xa2\xfe1\x7f\xae\x16\xa3\xee\x85,\r\x1d,\xf5(\xe8\xf98\xf2\xb3\x8b}\xdb\\\xfc!2_A<\xbc\x8a\xc8}\xf7r\xf8lI\xf1Q\xb0\xf7\x0c^\xf0\xe1\xb5\xda5C\xfc.\x0f\x85ZL\xae\x1e*Vr}\xb0\x13\xd7k\x08\xcc\xbfS\xd2^\x9e68\xaaR\xa9d\x8f\xffjc\xeb\xc9\x94Xl-\xaf\x14+oE\xdb\\\x93\x05\x0fCE\x8b\x90\xfc\x8ce\xdc\xf7_\x13\xaf\x0e\xc9\xaa\xc0\x89\xe4\xc8\x04\xfbp\xcah\xb7UY|\x9c\xf6\x8eO\xa8\xb1D\x84u\xa5\x8f\x95\xfcs@\xca\x92R\xeef\xd3\xb0X\xbbR\xd7/\xc9\x9e\x9cJ\xc3S\xc3\xa8\x9a\x89d\xf4\xe3<\x86\xba\x83c\x1e=o/\xfa|\xdbMVx?\xac\x08{n\x07\xe9\x0c\xafN\xbaVj\xa3\xe4\xcak\x0b\xf8\x9em\t\x97\xf9~\xef$&\xd1\xda%\x9a\x97\x02*\xef8\xca6\xa5\x17\x94&\xf4jH\xd6\x0f S\x1a\xa5\xd9\xdc\x7f\xfb8\xb2\xbc\xdf0\xa2\xd0\xae+\xe7\xce)_\xf2\xb5\'\x1d\xfcS\x88dH\xb2\xb8\x1f4:"f#\x94G\x86\x91\xcbL\xa6\xc1\xa4\x94\xa8\xbd\xd1\x95\xaf\xa2y\xb5%$VJ\x85S\xd6\x1f\x8d\x11\xe7\xa1\x15\xba\xeb\x841\x8d\x17iJ\xea:\xc6\xf7n\x9a\xc3\xd6\xdf&\xc4\xed\xb0fy\xbb\xb4\x9d\x06\x8c\xf9\x8e\xf7\xae\x1e\x01o\x9c\x87\x17\xcel=Aj|gn\x13\xc4\xf8A\xe2\x9b\xf7\x9ezS.\x95s\x9d{/\xe4>\xfc\x06\xdcL\xce\xe0\xc9g\x03_\xa4\xf1>\x84*\xfbk\\6\xffo\xbf`A\xba'
        self.pubkey = b'\xce\xa5\xab\xa7\xefE\xd2^\xcf\xad\x1f%\xda\xf3\xabyy\x19\x84\xba\x14V\x8f\x1c\x07b\r\x99e\xdf\x02\x1c:\x97t\xb5\x19\x13\xa9\xed\x0eJJu/\xae\x94\xe0u%H\xdd\x93F\xc5\xe9B\\D\xff\xae\xd1\xa6\xbc\xbe\x81'

        self.signature = b"\xf3\xe8`\x11\',\xc4\xa0\xb7\xdb\x1adl\x19\xd2\xf6{\xcfL\x1d!\xc9\xa9\xb9>M\xea\x8f\xc4\'[l\x8c\xc3\x1e\xdc\xb3*U\xf2n\xcf^\x16F-<\xfb\x0b\xc6\xb5@ -Nn\x14\xc2\xc7\xde\x96\xf3| c\x013\xb6\xd0\x93\xe3qD\x8e\xba\x1d\x1a\xc5=\x0c\xb8\x1a\xcd`\x0f\x10S\xa58\x85\x12\xaae\xb8\x14\xf8\x84*A\xee\xc54\xa0E\xcem\tt\x00U\x12\xe0\x05\x04\x89y]\x94\x82e\x9e\\v\x81L\xea?,\xfa\x1a\x1f\x00"
        self.ed521 = get_Ed521()

    def test_crypto_signing(self):
        signature = self.ed521.sign(self.privkey, self.pubkey, self.data)
        self.assertEqual(signature, self.signature)
