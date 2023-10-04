# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 15:36:41 2023

@author: 79245
"""

import math

def calculate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return str(e)

def length_unit_converter():
    print("长度单位换算")
    print("可用单位:")
    print("1. 米 (m)")
    print("2. 厘米 (cm)")
    print("3. 毫米 (mm)")
    print("4. 千米 (km)")
    print("5. 英尺 (ft)")
    
    choice = input("请选择要转换的单位 (1/2/3/4/5): ")
    value = float(input("请输入要转换的数值: "))
    
    if choice == '1':
        meters = value
        centimeters = value * 100
        millimeters = value * 1000
        kilometers = value / 1000
        feet = value * 3.28084
        print(f"{meters} 米 = {centimeters} 厘米 = {millimeters} 毫米 = {kilometers} 千米 = {feet} 英尺")
    elif choice == '2':
        centimeters = value
        meters = value / 100
        millimeters = value * 10
        kilometers = value / 100000
        feet = value * 0.0328084
        print(f"{centimeters} 厘米 = {meters} 米 = {millimeters} 毫米 = {kilometers} 千米 = {feet} 英尺")
    elif choice == '3':
        millimeters = value
        meters = value / 1000
        centimeters = value / 10
        kilometers = value / 1000000
        feet = value * 0.00328084
        print(f"{millimeters} 毫米 = {meters} 米 = {centimeters} 厘米 = {kilometers} 千米 = {feet} 英尺")
    elif choice == '4':
        kilometers = value
        meters = value * 1000
        centimeters = value * 100000
        millimeters = value * 1000000
        feet = value * 3280.84
        print(f"{kilometers} 千米 = {meters} 米 = {centimeters} 厘米 = {millimeters} 毫米 = {feet} 英尺")
    elif choice == '5':
        feet = value
        meters = value / 3.28084
        centimeters = value / 0.0328084
        millimeters = value / 0.00328084
        kilometers = value / 3280.84
        print(f"{feet} 英尺 = {meters} 米 = {centimeters} 厘米 = {millimeters} 毫米 = {kilometers} 千米")
    else:
        print("无效的选择，请重新选择。")

def mass_unit_converter():
    print("质量单位换算")
    print("可用单位:")
    print("1. 公斤 (kg)")
    print("2. 克 (g)")
    print("3. 毫克 (mg)")
    print("4. 吨 (ton)")
    print("5. 磅 (lb)")
    
    choice = input("请选择要转换的单位 (1/2/3/4/5): ")
    value = float(input("请输入要转换的数值: "))
    
    if choice == '1':
        kilograms = value
        grams = value * 1000
        milligrams = value * 1000000
        tons = value / 1000
        pounds = value * 2.20462
        print(f"{kilograms} 公斤 = {grams} 克 = {milligrams} 毫克 = {tons} 吨 = {pounds} 磅")
    elif choice == '2':
        grams = value
        kilograms = value / 1000
        milligrams = value * 1000
        tons = value / 1000000
        pounds = value * 0.00220462
        print(f"{grams} 克 = {kilograms} 公斤 = {milligrams} 毫克 = {tons} 吨 = {pounds} 磅")
    elif choice == '3':
        milligrams = value
        kilograms = value / 1000000
        grams = value / 1000
        tons = value / 1000000000
        pounds = value * 0.00000220462
        print(f"{milligrams} 毫克 = {kilograms} 公斤 = {grams} 克 = {tons} 吨 = {pounds} 磅")
    elif choice == '4':
        tons = value
        kilograms = value * 1000
        grams = value * 1000000
        milligrams = value * 1000000000
        pounds = value * 2204.62
        print(f"{tons} 吨 = {kilograms} 公斤 = {grams} 克 = {milligrams} 毫克 = {pounds} 磅")
    elif choice == '5':
        pounds = value
        kilograms = value / 2.20462
        grams = value / 0.00220462
        milligrams = value / 0.00000220462
        tons = value / 2204.62
        print(f"{pounds} 磅 = {kilograms} 公斤 = {grams} 克 = {milligrams} 毫克 = {tons} 吨")
    else:
        print("无效的选择，请重新选择。")

while True:
    result = None  # 用于存储上一次计算的结果
    
    print("科学计算器")
    
    while True:
        print("可用操作:")
        print("1. 多项式四则运算")
        print("2. 计算三角函数")
        print("3. 计算阶乘")
        print("4. 计算平方")
        print("5. 计算平方根")
        print("6. 计算绝对值")
        print("7. 长度单位换算")
        print("8. 质量单位换算")
        print("9. 清零")
        print("10. 退出")
        
        choice = input("请选择要执行的操作 (1/2/3/4/5/6/7/8/9/10): ")
        
        if choice == '1':
            expression = input("请输入要计算的多项式表达式: ")
            result = calculate_expression(expression)
            print("结果:", result)
        elif choice == '2':
            angle_deg = float(input("请输入角度值: "))
            angle_rad = math.radians(angle_deg)
            print("sin({}°) = {:.2f}".format(angle_deg, math.sin(angle_rad)))
            print("cos({}°) = {:.2f}".format(angle_deg, math.cos(angle_rad)))
            print("tan({}°) = {:.2f}".format(angle_deg, math.tan(angle_rad)))
            print("cot({}°) = {:.2f}".format(angle_deg, 1 / math.tan(angle_rad)))
            print("sec({}°) = {:.2f}".format(angle_deg, 1 / math.cos(angle_rad)))
            print("csc({}°) = {:.2f}".format(angle_deg, 1 / math.sin(angle_rad)))
        elif choice == '3':
            num = int(input("请输入一个整数: "))
            result = math.factorial(num)
            print("{}的阶乘是: {}".format(num, result))
        elif choice == '4':
            num = float(input("请输入一个数字: "))
            result = num ** 2
            print("{}的平方是: {:.2f}".format(num, result))
        elif choice == '5':
            num = float(input("请输入一个非负数: "))
            if num >= 0:
                result = math.sqrt(num)
                print("{}的平方根是: {:.2f}".format(num, result))
            else:
                print("请输入一个非负数。")
        elif choice == '6':
            num = float(input("请输入一个数字: "))
            result = abs(num)
            print("{}的绝对值是: {:.2f}".format(num, result))
        elif choice == '7':
            length_unit_converter()
        elif choice == '8':
            mass_unit_converter()
        elif choice == '9':
            result = None  # 清零
            print("已清零。")
        elif choice == '10':
            print("退出计算器。")
            break
        else:
            print("无效的选择，请重新选择。")

        # 在每次计算后询问用户是否要使用上一次的结果进行下一次计算
        if result is not None:
            next_calculation = input("要使用上一次的结果进行下一次计算吗？(Y/N): ")
            if next_calculation.lower() == 'y':
                expression = input("请输入要进行的下一次计算表达式: ")
                expression = expression.replace("ans", str(result))  # 将"ans"替换为上一次的结果
                result = calculate_expression(expression)
                print("结果:", result)

    restart = input("要重新开始计算吗？(Y/N): ")
    if restart.lower() != 'y':
        print("退出程序。")
        break







