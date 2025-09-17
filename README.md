Проект "Спираль" написан на языке Python при помощи библиотеки tkinter 
из библиотеки tkinter были задействованы модули такие как canvas , after , mainloop ,pack , title 

canvas - создание холста на котором будут происходить манипуляции с рисованием спирали
canvas = tk.canvas(window, width = 600 , height = 600) # размер холста 600x600

<img width="543" height="582" alt="image" src="https://github.com/user-attachments/assets/29860c3b-f07c-4bec-975a-d3cafabab7c8" />


after - метод  используется для анимации window.after(ms,func): ms - через какое количество миллисекунд будет запущена функция переданная в метод
<img width="311" height="238" alt="image" src="https://github.com/user-attachments/assets/3c7597f1-e00c-48a1-9a07-68bd80bcc963" />
<img width="379" height="317" alt="image" src="https://github.com/user-attachments/assets/1f51e6c4-5e3c-45ae-b20b-41560223d8d4" />


mainloop  - метод запускает действия которые происходят, с помощью его видим окошко tkinter

pack - метод сохраняет изменения , то есть запаковывает и отображает на холсте

create_oval - создает овал из 4 координат canvas.create_oval(x1,y1,x2,y2)
<img width="511" height="546" alt="image" src="https://github.com/user-attachments/assets/049aeaef-4914-40e9-ac75-7cd9ab3938dd" />
