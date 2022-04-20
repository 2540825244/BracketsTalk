#*语-10版加密及解密

zero = "["
one = "]"
fill_zero = True
space = " "
end = False

def main():
    global end
    while not end:
        selection = input("请选择功能[1=加密, 2=解密, 3=自定义选项, 4=退出]: ")
        if(selection == "1"):
            text = str(input("请输入要加密的文字: "))
            output = encrypt(text)
            input(f"输出: {output}\n按回车键返回")
        elif(selection == "2"):
            text = str(input("请输入要解密的文字: "))
            output = decrypt(text)
            input(f"输出: {output}\n按回车键返回")
        elif(selection == "3"):
            advanced()
        elif(selection == "4"):
            input("按回车键退出")
            end = True
        else:
            input("错误: 未选择已有功能\n按回车键返回")

def advanced():
    global zero
    global one
    global fill_zero
    global space
    while True:
        selection = input("请选择操作[1=返回, 2=更改0, 3=更改1, 4=选择是否填充0, 5=选择字节之间字符]: ")
        if(selection == "1"):
            return
        elif(selection == "2"):
            zero = input(f"请选择新的0 (当前为{zero}): ")
        elif(selection == "3"):
            one = input(f"请选择新的0 (当前为{one}): ")
        elif(selection == "4"):
            selection_further = input(f"请选择是否在密码面前添加0[1=是, 2/任意其它=否](当前为{fill_zero}): ")
            if(selection_further == "1"):
                fill_zero = True
            else:
                fill_zero = False
        elif(selection == "5"):
            space = str(input(f"请选择新的字节区分符(当前为{space}): "))
        else:
            input("错误: 未选择已有功能\n按回车键返回")


def encrypt(text):
    global zero
    global one
    global fill_zero 
    global space

    list_text = []
    list_text[:0] = text
    list_code = []
    list_encrypted = []

    for char in list_text:
        list_code.append(bin(int(ord(char)))[2::])
    
    for code in list_code:
        encrypted = ""
        if(fill_zero):
            while len(code) < 16:
                code = "0" + code
        
        for bit in code:
            if bit == "0":
                encrypted = encrypted + zero
            else:
                encrypted = encrypted + one

        list_encrypted.append(encrypted)

    return space.join(list_encrypted)

def decrypt(text):
    global zero
    global one
    global fill_zero
    global space

    if not all(c in [zero, one, space] for c in text):
        return "错误: 输入字符串拥有未定义的字符"

    list_separated = text.split(space)
    list_decrypted = []
    list_plain = []

    for encrypted in list_separated:
        encrypted = encrypted.replace(zero,"0")
        encrypted = encrypted.replace(one,"1")

        list_decrypted.append(encrypted)

    for decrypted in list_decrypted:
        list_plain.append(chr(int(decrypted,2)))

    return "".join(list_plain)

main()
