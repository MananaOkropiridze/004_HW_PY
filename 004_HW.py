################## HomeWork - listebi da funqciebi #############


######## 1 ) დაწერეთ პროგრამა ფუნქციის შესაქმნელად, 
######## func1()არგუმენტების ცვლადი სიგრძის მისაღებად და მათი მნიშვნელობის დასაბეჭდად.
# def funcVar(x):
#     lenVar = len (x)  
#     print (str (x) + ' contains ' + str(lenVar) + ' Characters')    
# funcVar (input ('Please Input Argument - '))


######## 2) დაწერეთ პროგრამა ისეთი ფუნქციის შესაქმნელად calculation(), 
######## რომ მას შეუძლია მიიღოს ორი ცვლადი და გამოთვალოს შეკრება და გამოკლება. 
######## ასევე, მან უნდა დააბრუნოს როგორც შეკრება, ასევე გამოკლება ერთი დაბრუნების გამოძახებით .
######## მოცემული :
######## def calculation(a, b):
########    # chasvit kodi
######## res = calculation(40, 10)
######## print(res)
## ver-a
# def caclulator (a, b):  
#     addition_ab = a + b
#     subtract_ab = a - b
#     return addition_ab, subtract_ab
# res = caclulator (int (input ('Please input numb1 -  ')), int (input ('Please input numb2 -  ')))
# print (res)
## ver-b მე ასეც მინდოდა რომ გამეკეთებინა. დავალებას ასრულებს, მაგრამ ხომ არ არის რაიმე ზოგადი ხარვეზი მსგავს ჩანაწერში?  
# def caclulator (a, b):  
#     addition_ab = a + b
#     subtract_ab = a - b
#     print (str (a) + ' plus ' + str (b) + ' is ' + str (addition_ab))
#     print (str (a) + ' mimus ' + str (b) + ' is ' + str (subtract_ab))
# caclulator (int (input ('Please input numb1 -  ')), int (input ('Please input numb2 -  ')))


######## 3) შექმენით ფუნქცია default არგუმენტით
######## დაწერეთ show_employee()შემდეგი პირობების გამოყენებით.
######## ფუნქციამ უნდა მიიღოს თანამშრომლის სახელი და ხელფასი და გამოსახოს ორივე.
######## თუ ფუნქციის გამოძახებისას ხელფასი აკლია, მაშინ ხელფასს მიანიჭეთ default მნიშვნელობა 9000
######## showEmployee("ana", 12000)
######## showEmployee("maria", 9000)
# def show_employee(name, salary):
#     if salary == '':
#         salary = 9000
#     print (name +"'s salary is " + str (salary) + ' GEL')
# show_employee(input ('Please input name -  '), input ('Please input salary -  '))


######## 4) შექმენით შიდა ფუნქცია შეკრების გამოსათვლელად შემდეგნაირად
########     შექმენით გარე ფუნქცია, რომელიც მიიღებს ორ პარამეტრს a და b
########     შექმენით შიდა ფუნქცია გარე ფუნქციის შიგნით, რომელიც გამოთვლის aდაb
########     და ბოლოს, გარე ფუნქცია დაამატებს 5-ს და დააბრუნებს მას
# def func_res(a, b): 
#     def a_add_b (a, b):
#        return a + b
#     sub_res = a_add_b (a, b)
#     return sub_res + 5
# final_res = func_res(int (input ('Please input number A -  ')), int (input ('Please input number B -  ')))
# print (final_res)


######## 5) მიანიჭეთ ფუნქციის ახალი სახელი 
######## ქვემოთ მოცემულია ფუნქცია display_student(name, age). 
######## show_tudent(name, age) მიანიჭეთ მას ახალი სახელი და გამოიძახეთ ის ახალი სახელის გამოყენებით.
######## def display_student(name, age):
########     print(name, age)
######## display_student("giorgi", 26)
# def display_student(name, age):
#     print (name + ' is ' + str (age) + ' years old')
#     print (name + ' lives in Rustavi for ' + str (age) + ' years')
# display_student ('Manana', '43')
# show_student = display_student # ახალ ფინქციას მიენიჭა ძველის სახელი და მიიღო ძველისგან ყველა ფუნქციის შესრულების ვალდებულება  
# show_student  ('Manana', '42')


######## 6) შექმენით ლისთი ყველა ლუწი რიცხვით 4-დან 30-მდე
######## output : [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
# ver-a (მარტივად):
# print(list(range(4, 30, 2)))
## ver-b.    for-ის გამოყენებით, ასეც მაინტერესებდაა:
# numbers = []
# for i in range (4,30):
#     if i % 2 == 0:
#         numbers.append(i)
# print (numbers)


######## 7) იპოვეთ ყველაზე დიდი ელემენტი მოცემული ლისთიდან  ???????
######## x = [4, 6, 8, 24, 12, 2]
# x = [4, 6, 8, 24, 12, 2]
# print (max(x))


######## 8) დაწერეთ პროგრამა რომელიც შეაჯამებს ყველა ელემენტს ლისთში
# x = [4, 6, 8, 24, 12, 2]
# sum = 0
# for i in x:
#     sum += i 
# print (sum)


######## 9) შექმენით სტრიქონი, რომელიც შედგება პირველი, შუა და ბოლო სიმბოლოსგან
######## str1 = "James"
######## output = Gri ??? ალბათ ეს უნდა იყოს აუთფუთი: output = Jms. str1-ის მიხედვით მასე გამოდის
# str1 = "James"
# frst = 0
# midd = len (str1) // 2
# last = len (str1) - 1
# print ('Main streeng is: ' + str1)
# print ('New streeng is: ' + str1[frst] + str1[midd] + str1[last])


######## 10) დაამატეთ ახალი სტრიქონი მოცემული სტრიქონის შუაში
######## s1 = "python"
######## s2 = "java"
######## output : pytjavahon
# def mrg_str1_str2 (str1, str2):
#     mid = len(str1) // 2
#     print ('Original 2strings are: ' + str1 + ' and ' + str2)
#     print ('Generated string is: ' + str1 [0: mid] + str2 + str1 [mid : len(str1)])
# mrg_str1_str2 ('python', 'java')