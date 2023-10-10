Дааная программа вырезает красные объекты и меняет их цвет на желтый.
Первым шагом мы загружаем наше изображение и переводим его в цветовое пространство HSV
Потом маска красного цвета, которая ищет оттенки красного в заданном нами диапазоне (верхняя и нижняя граница)
Далее мы применяем эту маску к нашей картинке и остается только красный объект — в нашем случае красное яблоко. Применяем мы ее с помощью 
команды result = cv2.bitwise_and(src, src, mask=mask_red), то есть происходит побитовое "И" между пикселями. В результате выполнения этой строки result будет 
содержать только те пиксели из src, которые соответствуют маске mask_red. 
Далее мы создаем зеленый цвет — параметры: 60 (оттенок), 255 (насыщенность), 255 (яркость). 
Функция green_mask = np.zeros_like(src) создает черно-белое изображение (green_mask) с такими же размерами и типом данных, как и исходное 
изображение. Начальное черно-белое изображение состоит из нулей. 
В функция green_mask[mask_red != 0] = green_color создается маска на основе ранее созданной маски mask_red, которая содержит True для всех пикселей,
которые были выделены как красный цвет. 
Далее для всех пикселей True устанавливаем соответствующий пиксель в green_color.  Это приводит к тому, что только выделенный красный объект будет окрашен в 
зеленый цвет, остальные пиксели останутся черными.
Конечным шагом бы объединяем наш первый результат (вырезанное красное яблоко) и маску зеленого с помощью функции add. Это приводит к тому, 
что красный объект на исходном изображении окрашивается в зеленый цвет.
![image](https://github.com/Anfysa/filter-image/assets/104844855/3587acfa-d516-4a53-b9b5-a46f3029c22b)
