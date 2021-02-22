# function paraBuilder(obj) {
#   var paras = "";
#   var notNullObj = obj || {};
#   var loop = 0;
#   for (var p in notNullObj) {
#     if (loop == 0) {
#       paras += '"' + p + '":"' + notNullObj[p] + '"';
#     } else {
#       paras += ',"' + p + '":"' + notNullObj[p] + '"';
#     }
#     loop += 1;
#   }
#   paras = "{" + paras + "}";
#   return paras;
# }


def para_builder(obj):
    paras = ""
    not_null_obj = obj if obj else {}
    loop = 0
    for i, p in enumerate(not_null_obj):
        if loop == 0:
            paras += '"' + str(i) + '":"' + p + '"'
        else:
            paras += ',"' + str(i) + '":"' + p + '"'
        loop += 1
    paras = "{" + paras + "}"
    return paras


class PC1(object):
    def __init__(self):
        self.bytesToHexChars = "0123456789abcdef"

    def hex_chars_to_bytes(self):
        C = [0 for _ in range(256)]
        for D in range(10):
            C[48 + D] = D
        for D in range(6):
            C[97 + D] = 10 + D
            C[65 + D] = 10 + D
        return C

    """
    encrypt: function (F, D) {
    var E = this.pc1(this.hexToBytes(F), this.hexToBytes(D), false);
    return this.bytesToHex(E);
  },
    """
    def encrypt(self,F,D):
        pass

    """
    if (typeof Z == "string" || typeof R == "string") {
      throw "invalid data tyep: src or key";
    }
    var b = R.length;
    var W = Z.length;
    if (b != 16) {
      throw "Key length should be 16";
    }
    var a = new Array();
    var X = new Array();
    var d;
    var T = 0,
      c = 0;
    var S = 0;
    for (d = 0; d < 8; ++d) {
      X[d] = (R[d << 1] << 8) | R[(d << 1) + 1];
    }
    for (d = 0; d < W; ++d) {
      var V = 0,
        Q = 0;
      var U;
      for (var Y = 0; Y < 8; ++Y) {
        V ^= X[Y];
        c = (c + Y) * 20021 + T;
        T = (V * 346) & 65535;
        c = (c + T) & 65535;
        V = (V * 20021 + 1) & 65535;
        Q ^= V ^ c;
      }
      U = Z[d];
      if (!P) {
        S = U * 257;
      }
      U = (U ^ (Q >> 8) ^ Q) & 255;
      if (P) {
        S = U * 257;
      }
      for (Y = 0; Y < 8; ++Y) {
        X[Y] ^= S;
      }
      a[d] = U;
    }
    return a;
  },
    """
    def pc1(self,Z, R, P):
        if isinstance(Z,str) or isinstance(R,str):
            raise Exception("invalid data tyep: src or key")
        b=len(R)
        W=len(Z)
        if b!=16:
            raise Exception("Key length should be 16")



def encrypt():


def get_epub_url(url, book_id, chapter_id, read_type):
    pass
