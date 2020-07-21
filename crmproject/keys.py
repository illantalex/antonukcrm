from cryptography.fernet import Fernet

_key = b'0hjIj_eSOa5O2qtdEBBu0ranhE5AzpaXoYzV0eziBlE='
_cipher_suite = Fernet(_key)

SECRET_KEY = _cipher_suite.decrypt(b'gAAAAABfFuBN20CX7J-f2Bqpvvto_FNkWIhEMY4UF4FCBMrGfP7zYztsmgycmZZvetWxTEsPpk9EPpEsuojEzJc-25RNZB6DSGvwPLfAXmb-_CoDTh0ZXXqV2Xr1NVZj_uSe1LWhRJknZFDVWIJqbQq8Sc8ciFzJfg==').decode("utf-8")
DEBUG = _cipher_suite.decrypt(b'gAAAAABfFuIMyklnvabg52WFc7ItizbO5_IdoQENj1XNuYHsAApUFXMJJpYraRRKHYAGJN8vhZO3i-skGD4FTSL2ubZWXLDMqg==').decode("utf-8")
AWS_ACCESS_KEY_ID = _cipher_suite.decrypt(b'gAAAAABfFuLcwvCbN32GBD3bOyFZBUdIabdlTFUt6VAy3pSdDpIyoOw9TT7c_uKZKRmNrNHdJq0-mRfAf1HvQHK6uS1y2IjVOunnS-HvAUzitE6E42hszTQ=').decode("utf-8")
AWS_SECRET_ACCESS_KEY = _cipher_suite.decrypt(b'gAAAAABfFuNfpUDL46jCBav3kNOwF_uRbM01X29VlwtoP9f60I6mz5VZBf1JpwDhfKDh_NWM2E3Yw3BrZu2URynfSdwfn3bKdSjJekcHTF3N9wHFISqqB6hBGvu76GeL4_Lecw88n3uh').decode("utf-8")
