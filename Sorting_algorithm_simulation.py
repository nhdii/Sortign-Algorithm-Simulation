from tkinter import *
from tkinter import ttk
import time
import random

root = Tk()
root.title("Sorting Algorithms Visualization")
root.maxsize(2000, 900)  
# config dung de tao thuoc tinh bg cho cua so
root.configure(bg = "#87A7FF")

algo_name = StringVar()     #Stringvar(): la ham dung de tao va truy cap bien trong tkinter
algo_list = ["Selection Sort", "Bubble Sort", "Insertion Sort", "Merge Sort"]

speed_name = StringVar()
speed_list = ["Slow", "Medium", "Fast"]

cre_arr = StringVar()
cre_arr_list = ["From file", "Random", "From Keyboard"]
# Tao array
arr = []

# Ham hien thi hinh khoi array
def display_Array(arr, colorArray):
    canvas.delete("all")
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
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x2, y2, text=arr[i])

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

#region Hàm Random Array 
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
#endregion

#region Hàm lấy Array từ file
def file_Array():
    global arr

    file = open("array.txt", "r")
    x = file.read()
    arr = x.split()

    for i in range(len(arr)):
        arr[i] = int(arr[i])

    display_Array(arr, ["#AE8EBB" for x in range(len(arr))])
    file.close()
#endregion

#region Hàm nhập giá trị Array từ bàn phím
def add_value_arr():
    global arr
    value = input_arr.get()
    arr = [int(i) for i in value.split()]
    display_Array(arr, ["#AE8EBB" for x in range(len(arr))])

def input_Arr():
    global input_arr
    window = Tk()
    window.maxsize(1000, 500)
    lb1 = Label(window, text="Nhập các giá trị cách nhau bởi khoảng trắng!")
    lb1.grid(row=0, column=1, padx=10, pady=5)
    lb2 = Label(window, text="Values: ")
    lb2.grid(row=1, column=0, padx=10, pady=5)

    input_arr = Entry(window, width=50)
    input_arr.grid(row=1, column=1, padx=10, pady=5)
    input_arr.focus()

    btn_add_value = Button(window, text="Add", command = add_value_arr)
    btn_add_value.grid(row=1, column=2, padx=10)
#endregion

def show_code():
    if algo_comboBox.get() == "Selection Sort":
        display_code.delete(0, END)
        algo_code_list = ['for i = 0 to n - 1:',
                          '    set min_idx = i',
                          '    for j = i + 1 to n:',
                          '        if (arr[min_idx] > arr[j]) then:',
                          '            set min_idx = j',
                          'Swap arr[i], arr[j]']
        [display_code.insert(END, item) for item in algo_code_list]
    elif algo_comboBox.get() == "Bubble Sort":
        display_code.delete(0, END)
        algo_code_list = ['for i to n:',
                          '    for j = 0 to n-i-1:',
                          '        if (arr[j] > arr[j+1]) then:',
                          '            Swap arr[j], arr[j+1]']
        [display_code.insert(END, item) for item in algo_code_list]
    elif algo_comboBox.get() == "Insertion Sort":
        display_code.delete(0, END)
        algo_code_list = ['for i = 1 to n:',
                          '    set key = arr[i]',
                          '    set j = i - 1',
                          '    while (j >= 0 and key < arr[j]',
                          '        set arr[j+1] = arr[j]',
                          '        j -= 1',
                          '    set arr[j+1] = key']   
        [display_code.insert(END, item) for item in algo_code_list]
    elif algo_comboBox.get() == "Merge Sort":
        display_code.delete(0, END)
        algo_code_list = ['mergesort(arr[], l, r',
                          'if r > l',
                          '    1. Tìm chỉ số nằm giữa mảng để chia mảng thành 2 nửa:',
                          '        middle m = (l+r)/2',
                          '    2. Gọi đệ quy hàm mergeSort cho nửa đầu tiên:',
                          '        mergeSort(arr, l, m)',
                          '    3. Gọi đệ quy hàm mergeSort cho nửa thứ hai:',
                          '        mergeSort(arr, m+1, r)',
                          '    4. Gộp 2 nửa mảng đã sắp xếp ở (2) và (3):',
                          '        merge(arr, 1, m, r)']
        [display_code.insert(END, item) for item in algo_code_list]
        
def create_Array():
    if cre_arr_comboBox.get() == "From file":
        file_Array()
    elif cre_arr_comboBox.get() == "Random":
        random_Array()
    elif cre_arr_comboBox.get() == "From Keyboard":
        input_Arr()


# function merge sort algorithm
def merge(arr, begin, mid, end):
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

def merge_sort(arr, begin, end, display_Array, tym):
    if begin < end:
        mid = int((begin + end)/2)
        merge_sort(arr, begin, mid, display_Array, tym)
        merge_sort(arr, mid + 1, end, display_Array, tym)
        merge(arr, begin, mid, end)
        display_Array(arr, ["green" if x >= begin and x < mid else "yellow" if x == mid  else "red" if x > mid and x <=end else "#AE8EBB" for x in range(len(arr))])
        time.sleep(tym)

    display_Array(arr, ["#01D38E" for x in range(len(arr))])

# Ham Merge Sort Des
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
    
# Ham sap xep tang dan
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
        merge_sort(arr, 0, len(arr)-1, display_Array, tym)

# Ham sap xep giam dan
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
       

# Tao widget chua cac widget lua chon thuat toan va toc do

display_window = Frame(root, width=300, height=200, bg="#242A53")
display_window.grid(row=0, column=0, padx=25, pady=50, sticky=NW)

# Hien thi danh sach lua chon cac thuat toan co nhan la Algorithm
label1 = Label(display_window, text="Algorithm: ", bg="white")
label1.grid(row=0, column=0, padx=10, pady=5, sticky=W)

# Combobox la hop chon 
algo_comboBox = ttk.Combobox(display_window, textvariable=algo_name, values = algo_list)
algo_comboBox.grid(row=0, column=1, padx=5, pady=5)
algo_comboBox.current(0)

# Hien thi danh sach lua chon toc do hien thi sap xep
label2 = Label(display_window, text="Sorting Speed: ", bg="white")
label2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_comboBox = ttk.Combobox(display_window, textvariable=speed_name, values=speed_list)
speed_comboBox.grid(row=1, column=1, padx=5, pady=5)
speed_comboBox.current(0)

# Label danh sach create array
label3 = Label(display_window, text = "Choose Array: ", bg = "white")
label3.grid(row=2, column=0, padx=10, pady=5, sticky=W)
cre_arr_comboBox = ttk.Combobox(display_window, textvariable=cre_arr, values=cre_arr_list)
cre_arr_comboBox.grid(row=2, column=1, padx=5, pady=5)
cre_arr_comboBox.current(0)

# Button Create Array
button1 = Button(display_window, text="Create Array", command = create_Array, bg="white")
button1.grid(row=0, column=2, pady=5)

# Button Sort Array
button2 = Button(display_window, text="Sort Ascending", command= sort_Asc, bg="white")
button2.grid(row=1, column=2, padx=5, pady=5)
button2 = Button(display_window, text="Sort descending", command= sort_Des, bg="white")
button2.grid(row=2, column=2, padx=5, pady=5)


# display_Code = Frame(root, width=400, height=200, bg="white")
# display_Code.grid(row=0, column=0, padx=25, pady=5, sticky=E)


display = Canvas(root, width=350, height=200, bg="white")
display.grid(row=0, column=0, padx=25, pady=5, sticky=E)
display_code = Listbox(display, width=40, height=7, font=("Times", 13))
display_code.grid(row=0, column=0, padx=10, pady=10)      

# Tien ich Canvas dung de tao widget hien thi cac hinh khoi Array
canvas = Canvas(root, width=800, height=400, bg="seashell")
canvas.grid(row=5, column=0, padx=10, pady=5)

root.mainloop()