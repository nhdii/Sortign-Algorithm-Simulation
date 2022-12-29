from tkinter import *
from tkinter import ttk
import time
import random

root = Tk()
root.title("Sorting Algorithms Visualization")
root.maxsize(2000, 900)  
root.configure(bg = "#87A7FF")

algo_name = StringVar()     #Stringvar(): là hàm dùng để truy cập biến trong Tkinter
algo_list = ["Selection Sort", "Bubble Sort", "Insertion Sort", "Merge Sort"]

speed_name = StringVar()
speed_list = ["Slow", "Medium", "Fast"]

cre_arr = StringVar()
cre_arr_list = ["From file", "Random", "From Keyboard"]
# Tao array
arr = []

# Hàm tạo các hình hộp chữ nhật từ các giá trị trong arr
def display_Array(arr, colorArray):
    arr_canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    width_x = canvas_width / (len(arr) + 1)     #Lấy kích thước của hình khối
    rectang_size = 20     
    space = 5
    get_arr = [i for i in arr]
    for i in range(len(arr)):
        x0 = i * width_x + space + rectang_size
        y0 = canvas_height - get_arr[i] 
        x1 = (i + 1) * width_x + rectang_size
        y1 = canvas_height
        x2 = (x0+x1)/2
        y2 = y0 + 10
        arr_canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        arr_canvas.create_text(x2, y2, text=arr[i])

    root.update_idletasks()


#region Hàm thiết lập tốc độ thực hiện sắp xếp
def set_speed():

    slow = 0.9
    medium = 0.05
    fast = 0.00005

    if speed_comboBox.get() == "Slow":
        return slow
    elif speed_comboBox.get() == "Medium":
        return medium
    elif speed_comboBox.get() =="Fast":
        return fast
#endregion

#region Tạo giá trị cho Arr
# Hàm tạo các giá trị ngẫu nhiên cho mảng
def random_Array():
    global arr
    array_size = 14
    start_value = 20
    end_value = 300

    arr = [122]
    for i in range(0, array_size):  
        random_arr = random.randint(start_value, end_value) #random các giá trị bắt đầu và kết thúc lớn hơn 0
        arr.append(random_arr)

    display_Array(arr, ["#AE8EBB" for x in range(len(arr))])

# Hàm lấy các giá trị trong Arr từ file
def file_Array():
    global arr

    file = open("array.txt", "r")
    x = file.read()
    arr = x.split()

    for i in range(len(arr)):
        arr[i] = int(arr[i])

    display_Array(arr, ["#AE8EBB" for x in range(len(arr))])
    file.close()

# Hàm nhập giá cho Arr từ bàn phím
def add_value_arr():
    global arr
    value = input_arr.get()
    arr = [int(i) for i in value.split()]
    display_Array(arr, ["#AE8EBB" for x in range(len(arr))])

def input_Arr():
    global input_arr
    window = Tk()
    window.maxsize(1000, 500)
    lb4 = Label(window, text="Nhập các giá trị cách nhau bởi khoảng trắng!")
    lb4.grid(row=0, column=1, padx=10, pady=5)
    lb5 = Label(window, text="Values: ")
    lb5.grid(row=1, column=0, padx=10, pady=5)

    input_arr = Entry(window, width=50)
    input_arr.grid(row=1, column=1, padx=10, pady=5)
    input_arr.focus()

    add_value_btn = Button(window, text="Add", command = add_value_arr)
    add_value_btn.grid(row=1, column=2, padx=10)
#endregion

# Hàm lấy giá trị từ combobox và trả về phương thức tạo giá trị cho Arr
def create_Array():
    if cre_arr_comboBox.get() == "From file":
        file_Array()
    elif cre_arr_comboBox.get() == "Random":
        random_Array()
    elif cre_arr_comboBox.get() == "From Keyboard":
        input_Arr()

#region Hàm hiển thị mã giả của các thuật toán
def show_code():
    if algo_comboBox.get() == "Selection Sort":
        code_lsb.delete(0, END)
        algo_code = ['for i = 0 to n - 1:',
                          '    set min_idx = i',
                          '    for j = i + 1 to n:',
                          '        if (arr[min_idx] > arr[j]) then:',
                          '            set min_idx = j',
                          'Swap arr[i], arr[j]']
        [code_lsb.insert(END, item) for item in algo_code]

    elif algo_comboBox.get() == "Bubble Sort":
        code_lsb.delete(0, END)
        algo_code = ['for i to n:',
                          '    for j = 0 to n-i-1:',
                          '        if (arr[j] > arr[j+1]) then:',
                          '            Swap arr[j], arr[j+1]']
        [code_lsb.insert(END, item) for item in algo_code]

    elif algo_comboBox.get() == "Insertion Sort":
        code_lsb.delete(0, END)
        algo_code = ['for i = 1 to n:',
                          '    set key = arr[i]',
                          '    set j = i - 1',
                          '    while (j >= 0 and key < arr[j]',
                          '        set arr[j+1] = arr[j]',
                          '        j -= 1',
                          '    set arr[j+1] = key']   
        [code_lsb.insert(END, item) for item in algo_code]

    elif algo_comboBox.get() == "Merge Sort":
        code_lsb.delete(0, END)
        algo_code = ['mergesort(arr[], l, r',
                          'if r > l',
                          '    1. Tìm chỉ số nằm giữa mảng để chia mảng thành 2 nửa:',
                          '        middle m = (l+r)/2',
                          '    2. Gọi đệ quy hàm mergeSort cho nửa đầu tiên:',
                          '        mergeSort(arr, l, m)',
                          '    3. Gọi đệ quy hàm mergeSort cho nửa thứ hai:',
                          '        mergeSort(arr, m+1, r)',
                          '    4. Gộp 2 nửa mảng đã sắp xếp ở (2) và (3):',
                          '        merge(arr, 1, m, r)']
        [code_lsb.insert(END, item) for item in algo_code]
#endregion

#region Các hàm gọi hàm sắp xếp
# Hàm thuật toán Merge Sort sắp xếp theo chiều tăng dần
def merge_asc(arr, begin, mid, end):
    p = begin
    q = mid + 1
    temp_Array = []

    for i in range(begin, end+1):
        if p > mid:
            temp_Array.append(arr[q])
            q += 1
        elif q > end:
            temp_Array.append(arr[p])
            p += 1
        elif arr[p] < arr[q]:
            temp_Array.append(arr[p])
            p += 1
        else:
            temp_Array.append(arr[q])
            q+=1
    for p in range(len(temp_Array)):
        arr[begin] = temp_Array[p]
        begin += 1

def merge_sort_asc(arr, begin, end, display_Array, tym):
    if begin < end:
        mid = int((begin + end)/2)
        merge_sort_asc(arr, begin, mid, display_Array, tym)
        merge_sort_asc(arr, mid + 1, end, display_Array, tym)
        merge_asc(arr, begin, mid, end)
        display_Array(arr, ["green" if x >= begin and x < mid else "yellow" if x == mid  else "red" if x > mid and x <=end else "#AE8EBB" for x in range(len(arr))])
        time.sleep(tym)

    display_Array(arr, ["#01D38E" for x in range(len(arr))])

# Hàm Sắp xếp giảm dần của thuật toán Merge Sort
def merge_des(arr, begin, mid, end):
    p = begin
    q = mid + 1
    temp_Array = []

    for i in range(begin, end+1):
        if p > mid:
            temp_Array.append(arr[q])
            q += 1
        elif q > end:
            temp_Array.append(arr[p])
            p += 1
        elif arr[p] > arr[q]:
            temp_Array.append(arr[p])
            p += 1
        else:
            temp_Array.append(arr[q])
            q+=1
    for p in range(len(temp_Array)):
        arr[begin] = temp_Array[p]
        begin += 1

def merge_sort_des(arr, begin, end, display_Array, tym):
    if begin < end:
        mid = int((begin + end)/2)
        merge_sort_des(arr, begin, mid, display_Array, tym)
        merge_sort_des(arr, mid + 1, end, display_Array, tym)
        merge_des(arr, begin, mid, end)
        display_Array(arr, ["green" if x >= begin and x < mid else "yellow" if x == mid  else "red" if x > mid and x <=end else "#AE8EBB" for x in range(len(arr))])
        time.sleep(tym)
    display_Array(arr, ["#01D38E" for x in range(len(arr))])
    
# Hàm sắp xếp tăng dần
def sort_Asc():
    tym = set_speed()
    #Bubble Sort algorithm
    if algo_comboBox.get() == "Bubble Sort":
        show_code()
        for i in range(len(arr)):
            for j in range(0, len(arr)-i-1):
                if (arr[j] > arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]  #SWAP
                    display_Array(arr, ["yellow" if x == j else "red" if x==j+1 else "#AE8EBB" for x in range(len(arr))])
                    time.sleep(tym)
        display_Array(arr, ["#01D38E" for x in range(len(arr))])
        
    # Selection sort algorithm
    elif algo_comboBox.get()=="Selection Sort":
        show_code()
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]  #SWAP
            display_Array(arr, ["green" if x == i else "red" if x == min_idx else "#AE8EBB" for x in range(len(arr))])
            time.sleep(tym)                      
        display_Array(arr, ["#01D38E" for x in range(len(arr))])

    # Insertion sort algorithm
    elif algo_comboBox.get()=="Insertion Sort":
        show_code()
        for i in range(1, len(arr)):     
            key = arr[i]
            j = i-1
            while (j >=0 and key < arr[j]):
                arr[j+1] = arr[j]
                j -= 1            
                display_Array(arr, ["yellow" if x == j else "red" if x==j+1 else "#AE8EBB" for x in range(len(arr))])
                time.sleep(tym)
            arr[j+1] = key
        display_Array(arr, ["#01D38E" for x in range(len(arr))])

    # Merge sort algorithm
    elif algo_comboBox.get() == "Merge Sort":
        show_code()
        merge_sort_asc(arr, 0, len(arr)-1, display_Array, tym)

# Hàm sắp xếp giảm dần
def sort_Des():
    tym = set_speed()
    #Bubble Sort algorithm
    if algo_comboBox.get() == "Bubble Sort":
        show_code()
        for i in range(len(arr)):
            for j in range(0, len(arr)-i-1):
                if (arr[j] < arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]  #SWAP
                    display_Array(arr, ["yellow" if x == j else "red" if x==j+1 else "#AE8EBB" for x in range(len(arr))])
                    time.sleep(tym)
        display_Array(arr, ["#01D38E" for x in range(len(arr))])
        
    # Selection sort algorithm
    elif algo_comboBox.get()=="Selection Sort":
        show_code()
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[min_idx] < arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]  #SWAP
            display_Array(arr, ["green" if x == i else "red" if x == min_idx else "#AE8EBB" for x in range(len(arr))])
            time.sleep(tym)                      
        display_Array(arr, ["#01D38E" for x in range(len(arr))])

    # Insertion sort algorithm
    elif algo_comboBox.get()== "Insertion Sort":
        show_code()
        for i in range(1, len(arr)):     
            key = arr[i]
            j = i - 1
            while (j >=0 and key > arr[j]):
                arr[j + 1] = arr[j]
                j -= 1            
                display_Array(arr, ["yellow" if x == j else "red" if x==j+1 else "#AE8EBB" for x in range(len(arr))])
                time.sleep(tym)
            arr[j + 1] = key
        display_Array(arr, ["#01D38E" for x in range(len(arr))])

    # Merge sort algorithm
    elif algo_comboBox.get() == "Merge Sort":
        show_code()
        merge_sort_des(arr, 0, len(arr)-1, display_Array, tym)
#endregion

#region Cài đặt giao diện
# Tạo widget chứa các widget label, button, combobox
display_window = Frame(root, width=300, height=200, bg="#242A53")
display_window.grid(row=0, column=0, padx=25, pady=50, sticky=NW)

# Label hiển thị dòng text "Algorithm: "
lb1 = Label(display_window, text="Algorithm: ", bg="white")
lb1.grid(row=0, column=0, padx=10, pady=5, sticky=W)

# Combobox hiển thị các thuật toán sắp xếp 
algo_comboBox = ttk.Combobox(display_window, textvariable=algo_name, values = algo_list)
algo_comboBox.grid(row=0, column=1, padx=5, pady=5)
algo_comboBox.current(0)

# Label hiển thị dòng text "Sorting Speed: " 
lb2 = Label(display_window, text="Sorting Speed: ", bg="white")
lb2.grid(row=1, column=0, padx=10, pady=5, sticky=W)

# Combobox hiển thị các lựa chọn tốc độ sắp xếp
speed_comboBox = ttk.Combobox(display_window, textvariable=speed_name, values=speed_list)
speed_comboBox.grid(row=1, column=1, padx=5, pady=5)
speed_comboBox.current(0)

# Label hiển thị đoạn text "Choose Array: "
lb3 = Label(display_window, text = "Choose Array: ", bg = "white")
lb3.grid(row=2, column=0, padx=10, pady=5, sticky=W)

# Combobox hiển thị các lựa chọn tạo mảng
cre_arr_comboBox = ttk.Combobox(display_window, textvariable=cre_arr, values=cre_arr_list)
cre_arr_comboBox.grid(row=2, column=1, padx=5, pady=5)
cre_arr_comboBox.current(0)

# Button dùng để tạo mảng
btn_cre_arr = Button(display_window, text="Create Array", command = create_Array, bg="white")
btn_cre_arr.grid(row=0, column=2, pady=5)

# Button sắp xếp tăng, giảm
sort_asc_btn = Button(display_window, text="Sort Ascending", command= sort_Asc, bg="white")
sort_asc_btn.grid(row=1, column=2, padx=5, pady=5)
sort_des_btn = Button(display_window, text="Sort descending", command= sort_Des, bg="white")
sort_des_btn.grid(row=2, column=2, padx=5, pady=5)

#Tạo widget chứa mã giả thuật toán 
code_lsb = Listbox(root, width=40, height=9, font=("Times", 13))
code_lsb.grid(row=0, column=0, padx=20, pady=10, sticky=E)      

# Tạo Canvas chứa widget tạo các hình khối của các giá trị trong mảng
arr_canvas = Canvas(root, width=800, height=400, bg="seashell")
arr_canvas.grid(row=5, column=0, padx=10, pady=5)

#endregion

root.mainloop()