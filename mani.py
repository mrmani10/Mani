# ENCRYPTED by PY-ENCODE
# Created by B14CK-KN1GH7 (NAFIS-FUAD)
# Facebook : http://facebook.com/nafis.fuad.904
# Github : http://github.com/nfs-tech-bd
 
import zlib,base64
exec(zlib.decompress(base64.b64decode("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")))
 
