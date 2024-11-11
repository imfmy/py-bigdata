"""
二进制数据处理：bytearray 是处理文件数据、网络数据和其他二进制内容的理想选择，因为二进制数据需要字节序列的支持，bytearray 允许字节数据的修改。
I/O 操作：例如，在文件和网络编程中，数据通常以字节的形式传输，bytearray 提供了一个易于修改的缓冲区。
字节级数据操作：因为 bytearray 是可变的，可以在字节级别进行加密、解密或压缩等操作。
编码与解码：bytearray 适合用在需要频繁编码、解码的场景，可以直接将字符串转为字节数组进行处理，然后在需要时进行解码。
"""

b = bytearray(b'hello world')
b2 = bytearray("hello world", "utf-8")
print(b == b2)
# True
print(type(b))
# <class 'bytearray'>
print(len(b))
# 11

# 创建一个长度为 5 的空字节数组，每个字节值为 0
b3 = bytearray(5)
print(b3)
# bytearray(b'\x00\x00\x00\x00\x00')

# 切片操作
print(b[0])
# 104
b[0]=97
print(b)
# bytearray(b'aello world')

# 追加数据：可以用 append()、extend() 方法或 += 操作符。
b = bytearray(b"hello")
b.append(33)
b.extend(b" world")
print(b)
# 输出: bytearray(b'hello! world')

# 转化为 bytes：可以通过 bytes() 方法将 bytearray 转换为不可变的 bytes。
b = bytearray(b"hello")
immutable_bytes = bytes(b)
print(immutable_bytes,type(immutable_bytes))
# b'hello' <class 'bytes'>

# 值范围限制：bytearray 的每个元素只能是 0-255 之间的整数（单字节表示），超过该范围会引发 ValueError
# print(bytearray(b"hello world你好"))
# SyntaxError: bytes can only contain ASCII literal characters.