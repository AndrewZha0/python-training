import jwt
import json
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

jwt_token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImZhODEzMTQ2LTVlZGQtNGU0Zi05ZjVlLThhZjQwNDI5ZDAwNHNpZyJ9.eyJpYXQiOjE3MTIzNzU4NzAsImV4cCI6MTc0MzkxMTg3MCwiaXNzIjoib2F1dGgyaWR0LWNuIiwianRpIjoiNDFiNDZmNjYtN2I0Ni00ZjQxLWFkZDMtMjljYmU4NjJjMWQ4IiwiYXVkIjoib2F1dGgyaWR0IiwidHJ1c3QiOjEwMCwibGF0IjoxNjU4OTE5Mjk4LCJjbGkiOiJkMjY3OWI1ODQzYzNmMmNkYjlkYzBkYzdlYzI5ZTNjNyIsInN1YiI6IjY1OWQwMWM1LWViODctNGFhNC05NDM5LTIxYTI0NzMyZmZkMyIsInNidCI6Im5pa2U6cGx1cyIsInNjcCI6WyJuaWtlLmRpZ2l0YWwiXSwicnNpZCI6IjFjMmVkNTViLWUzNDUtNGNjYy1iZjYxLWNkMjQyMTBjNmU4YSIsImxyc2NwIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgcGhvbmUgZmxvdyBvZmZsaW5lX2FjY2VzcyBuaWtlLmRpZ2l0YWwifQ.Yo1UoayfpZrErjETUUhbWc8FXeAIP4fy0NLvrpljaeKOubnmMG6GFG2Ygfm_mEaTJ67Bowc_vXn-8jY9ccclqpI9Bfy2--2maEMZoaDiV-TClQE7MnXMMeeOxIJz3I9V9J86Oq-ONt18QCTSYUSplX73y97j-OPmD0QEpp3BnNhha4UgrkfOHLkQEoISc826wItb7GjSs1LEX8c_cmGpg1evUl2Wd64RQbpVX2cM1LFCG_o_CS5SePlHiuaX8KZ97YPD2Sx1J0n2LtVlKafyn1oVIeMJlQeFFrVmQN8rPbl-8qgY5AiOzxCbZ27x4bPj56BwyfrBqzc8gIpxcgR8Ow'

pem_key1 = '''
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtA1oet+9f3jG/W3ZJ/GZ
wTlMD3LReHox2Gq68pf9j0cGT8ihAMU6hYnL/yx+A8RgkNYjQ2n22bHBJOrWnaz7
aGo9lS4+WJ7zRbdViYDbpxrqJoWGC+O+gRIAEu4zYNRZsvvd3peePguTqIlPLM32
PA6xqxf1XuqAtyq0B2feqBCehR3oLf2xaVQfRB3XoFP3vFliXLzcNmlYla2GbV7m
PYhKKKwQMy3t7UG5m8ED58XNooaJJ8pBNAA0SThVhSH9AEI9aLsID5Hm8l0cdDK4
Lc23zURJDvQlsllc8mvzY+ueKoq8lTx1k+oObRf7mrUkmJD45xyWCRxl2OB1UKTs
7QIDAQAB
-----END PUBLIC KEY-----
'''
pem_key = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtA1oet+9f3jG/W3ZJ/GZ\nwTlMD3LReHox2Gq68pf9j0cGT8ihAMU6hYnL/yx+A8RgkNYjQ2n22bHBJOrWnaz7\naGo9lS4+WJ7zRbdViYDbpxrqJoWGC+O+gRIAEu4zYNRZsvvd3peePguTqIlPLM32\nPA6xqxf1XuqAtyq0B2feqBCehR3oLf2xaVQfRB3XoFP3vFliXLzcNmlYla2GbV7m\nPYhKKKwQMy3t7UG5m8ED58XNooaJJ8pBNAA0SThVhSH9AEI9aLsID5Hm8l0cdDK4\nLc23zURJDvQlsllc8mvzY+ueKoq8lTx1k+oObRf7mrUkmJD45xyWCRxl2OB1UKTs\n7QIDAQAB\n-----END PUBLIC KEY-----\n"

# 加载公钥
public_key = serialization.load_pem_public_key(
    pem_key.encode('utf-8'),
    backend=default_backend()
)
print("公钥加载成功")

# 验证JWT签名
try:
    # 这里假设JWT没有加密，只是签名了
    # 如果JWT是签名的，则使用jwt.decode，如果是加密的，则先使用jwt.decode_encrypted
    decoded_token = jwt.decode(
        jwt_token,
        public_key,
        algorithms=['RS256'],  # 根据你的JWT签名算法来选择
        audience="oauth2idt"
    )
    print("Token is valid.")
    print(decoded_token)
except jwt.exceptions.DecodeError as e:
    print("Token is invalid:", e)
