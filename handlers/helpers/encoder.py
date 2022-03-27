import base64


class Encoder:

    @staticmethod
    def encode_as_base_64(msg: str, orig_charset='cp1251'):
        message_bytes = msg.encode(orig_charset)

        base64_bytes = base64.b64encode(message_bytes)
        return base64_bytes.decode(orig_charset)
