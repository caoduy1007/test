while True:
    tendangnhap = input("hay dien ten dang nhap cua ban vao:")
    password = input("Hay cai dat password cua ban:")
    passagain = input("hay nhap lai mat khau:")
    gmail = input("hay ngap dia chi gmail cua ban vao:")
    if password != passagain:
        print("ERROR.CHECK PASS. LOI ROI NHAP LAI DI")
    elif "@gmail.com" not in gmail:
        print("ERROR.SAI GMAIL. LOI ROI NHAP LAI DI")
    elif not (password.isdigit()):
        print("ERROR.SAI SO. LOI ROI NHAP LAI DI")
    elif not (password.isalpha()):
        print("ERROR.SAI CHU. LOI ROI NHAP LAI DI")
    elif not len(password) > 8:
        print("ERROR.THIEU PASS. LOI ROI NHAP LAI DI")
    else:
        print("DANG KI THANH CONG")
        break

