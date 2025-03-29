import customtkinter
import os
from PIL import Image

from modules import *


screen.geometry("700x700")


bg_color_text = customtkinter.CTkLabel(screen, text = "Background Color:", width= 75, height= 20, text_color= "white", font= (25, 25))





def sumbit_cmd():


    global matrix_strings, matrix_columns, final_matrix

    matrix_strings = [
        [],
        [],
        [],
        [],
        [],
        [],  
        [],
        [],
        [],
        [],
    ]

    matrix_columns = [
        [],
        [],
        [],
        [],
        [],
        [],  
        [],
        [],
        [],
        [],
    ]

    if button1_1._fg_color == "dark red":
        matrix_strings[0].append(1)
    else:
        matrix_strings[0].append(0)

    if button1_2._fg_color == "dark red":
        matrix_strings[0].append(1)
    else:
        matrix_strings[0].append(0)



    if button1_3._fg_color == "dark red":
        matrix_strings[0].append(1)
    else:
        matrix_strings[0].append(0)


    if button1_4._fg_color == "dark red":
        matrix_strings[0].append(1)
    else:
        matrix_strings[0].append(0)

    if button1_5._fg_color == "dark red":
        matrix_strings[0].append(1)
    else:
        matrix_strings[0].append(0)


    if button1_6._fg_color == "dark red":
        matrix_strings[0].append(1)
    else:
        matrix_strings[0].append(0)  

    if button1_7._fg_color == "dark red":
        matrix_strings[0].append(1)
    else:
        matrix_strings[0].append(0)


    if button1_8._fg_color == "dark red":
        matrix_strings[0].append(1)
    else:
        matrix_strings[0].append(0)

    if button1_9._fg_color == "dark red":
        matrix_strings[0].append(1)
    else:
        matrix_strings[0].append(0)

    if button1_10._fg_color == "dark red":
        matrix_strings[0].append(1)
    else:
        matrix_strings[0].append(0)  












    if button2_1._fg_color == "dark red":
        matrix_strings[1].append(1)
    else:
        matrix_strings[1].append(0)

    if button2_2._fg_color == "dark red":
        matrix_strings[1].append(1)
    else:
        matrix_strings[1].append(0)



    if button2_3._fg_color == "dark red":
        matrix_strings[1].append(1)
    else:
        matrix_strings[1].append(0)




    if button2_4._fg_color == "dark red":
        matrix_strings[1].append(1)
    else:
        matrix_strings[1].append(0)

    if button2_5._fg_color == "dark red":
        matrix_strings[1].append(1)
    else:
        matrix_strings[1].append(0)


    if button2_6._fg_color == "dark red":
        matrix_strings[1].append(1)
    else:
        matrix_strings[1].append(0)  

    if button2_7._fg_color == "dark red":
        matrix_strings[1].append(1)
    else:
        matrix_strings[1].append(0)


    if button2_8._fg_color == "dark red":
        matrix_strings[1].append(1)
    else:
        matrix_strings[1].append(0)

    if button2_9._fg_color == "dark red":
        matrix_strings[1].append(1)
    else:
        matrix_strings[1].append(0)


    if button2_10._fg_color == "dark red":
        matrix_strings[1].append(1)
    else:
        matrix_strings[1].append(0)  

















    if button3_1._fg_color == "dark red":
        matrix_strings[2].append(1)
    else:
        matrix_strings[2].append(0)

    if button3_2._fg_color == "dark red":
        matrix_strings[2].append(1)
    else:
        matrix_strings[2].append(0)



    if button3_3._fg_color == "dark red":
        matrix_strings[2].append(1)
    else:
        matrix_strings[2].append(0)


    if button3_4._fg_color == "dark red":
        matrix_strings[2].append(1)
    else:
        matrix_strings[2].append(0)

    if button3_5._fg_color == "dark red":
        matrix_strings[2].append(1)
    else:
        matrix_strings[2].append(0)


    if button3_6._fg_color == "dark red":
        matrix_strings[2].append(1)
    else:
        matrix_strings[2].append(0)  

    if button3_7._fg_color == "dark red":
        matrix_strings[2].append(1)
    else:
        matrix_strings[2].append(0)


    if button3_8._fg_color == "dark red":
        matrix_strings[2].append(1)
    else:
        matrix_strings[2].append(0)

    if button3_9._fg_color == "dark red":
        matrix_strings[2].append(1)
    else:
        matrix_strings[2].append(0)


    if button3_10._fg_color == "dark red":
        matrix_strings[2].append(1)
    else:
        matrix_strings[2].append(0)  



    if button4_1._fg_color == "dark red":
        matrix_strings[3].append(1)
    else:
        matrix_strings[3].append(0)

    if button4_2._fg_color == "dark red":
        matrix_strings[3].append(1)
    else:
        matrix_strings[3].append(0)



    if button4_3._fg_color == "dark red":
        matrix_strings[3].append(1)
    else:
        matrix_strings[3].append(0)


    if button4_4._fg_color == "dark red":
        matrix_strings[3].append(1)
    else:
        matrix_strings[3].append(0)

    if button4_5._fg_color == "dark red":
        matrix_strings[3].append(1)
    else:
        matrix_strings[3].append(0)


    if button4_6._fg_color == "dark red":
        matrix_strings[3].append(1)
    else:
        matrix_strings[3].append(0)  

    if button4_7._fg_color == "dark red":
        matrix_strings[3].append(1)
    else:
        matrix_strings[3].append(0)


    if button4_8._fg_color == "dark red":
        matrix_strings[3].append(1)
    else:
        matrix_strings[3].append(0)

    if button4_9._fg_color == "dark red":
        matrix_strings[3].append(1)
    else:
        matrix_strings[3].append(0)


    if button4_10._fg_color == "dark red":
        matrix_strings[3].append(1)
    else:
        matrix_strings[3].append(0)  
    





    if button5_1._fg_color == "dark red":
        matrix_strings[4].append(1)
    else:
        matrix_strings[4].append(0)

    if button5_2._fg_color == "dark red":
        matrix_strings[4].append(1)
    else:
        matrix_strings[4].append(0)



    if button5_3._fg_color == "dark red":
        matrix_strings[4].append(1)
    else:
        matrix_strings[4].append(0)


    if button5_4._fg_color == "dark red":
        matrix_strings[4].append(1)
    else:
        matrix_strings[4].append(0)

    if button5_5._fg_color == "dark red":
        matrix_strings[4].append(1)
    else:
        matrix_strings[4].append(0)


    if button5_6._fg_color == "dark red":
        matrix_strings[4].append(1)
    else:
        matrix_strings[4].append(0)  

    if button5_7._fg_color == "dark red":
        matrix_strings[4].append(1)
    else:
        matrix_strings[4].append(0)


    if button5_8._fg_color == "dark red":
        matrix_strings[4].append(1)
    else:
        matrix_strings[4].append(0)

    if button5_9._fg_color == "dark red":
        matrix_strings[4].append(1)
    else:
        matrix_strings[4].append(0)


    if button5_10._fg_color == "dark red":
        matrix_strings[4].append(1)
    else:
        matrix_strings[4].append(0)  





    if button6_1._fg_color == "dark red":
        matrix_strings[5].append(1)
    else:
        matrix_strings[5].append(0)

    if button6_2._fg_color == "dark red":
        matrix_strings[5].append(1)
    else:
        matrix_strings[5].append(0)



    if button6_3._fg_color == "dark red":
        matrix_strings[5].append(1)
    else:
        matrix_strings[5].append(0)


    if button6_4._fg_color == "dark red":
        matrix_strings[5].append(1)
    else:
        matrix_strings[5].append(0)

    if button6_5._fg_color == "dark red":
        matrix_strings[5].append(1)
    else:
        matrix_strings[5].append(0)


    if button6_6._fg_color == "dark red":
        matrix_strings[5].append(1)
    else:
        matrix_strings[5].append(0)  

    if button6_7._fg_color == "dark red":
        matrix_strings[5].append(1)
    else:
        matrix_strings[5].append(0)


    if button6_8._fg_color == "dark red":
        matrix_strings[5].append(1)
    else:
        matrix_strings[5].append(0)

    if button6_9._fg_color == "dark red":
        matrix_strings[5].append(1)
    else:
        matrix_strings[5].append(0)


    if button6_10._fg_color == "dark red":
        matrix_strings[5].append(1)
    else:
        matrix_strings[5].append(0)  











    if button7_1._fg_color == "dark red":
        matrix_strings[6].append(1)
    else:
        matrix_strings[6].append(0)

    if button7_2._fg_color == "dark red":
        matrix_strings[6].append(1)
    else:
        matrix_strings[6].append(0)



    if button7_3._fg_color == "dark red":
        matrix_strings[6].append(1)
    else:
        matrix_strings[6].append(0)


    if button7_4._fg_color == "dark red":
        matrix_strings[6].append(1)
    else:
        matrix_strings[6].append(0)

    if button7_5._fg_color == "dark red":
        matrix_strings[6].append(1)
    else:
        matrix_strings[6].append(0)


    if button7_6._fg_color == "dark red":
        matrix_strings[6].append(1)
    else:
        matrix_strings[6].append(0)  

    if button7_7._fg_color == "dark red":
        matrix_strings[6].append(1)
    else:
        matrix_strings[6].append(0)


    if button7_8._fg_color == "dark red":
        matrix_strings[6].append(1)
    else:
        matrix_strings[6].append(0)

    if button7_9._fg_color == "dark red":
        matrix_strings[6].append(1)
    else:
        matrix_strings[6].append(0)


    if button7_10._fg_color == "dark red":
        matrix_strings[6].append(1)
    else:
        matrix_strings[6].append(0)  






    if button8_1._fg_color == "dark red":
        matrix_strings[7].append(1)
    else:
        matrix_strings[7].append(0)

    if button8_2._fg_color == "dark red":
        matrix_strings[7].append(1)
    else:
        matrix_strings[7].append(0)



    if button8_3._fg_color == "dark red":
        matrix_strings[7].append(1)
    else:
        matrix_strings[7].append(0)


    if button8_4._fg_color == "dark red":
        matrix_strings[7].append(1)
    else:
        matrix_strings[7].append(0)

    if button8_5._fg_color == "dark red":
        matrix_strings[7].append(1)
    else:
        matrix_strings[7].append(0)


    if button8_6._fg_color == "dark red":
        matrix_strings[7].append(1)
    else:
        matrix_strings[7].append(0)  

    if button8_7._fg_color == "dark red":
        matrix_strings[7].append(1)
    else:
        matrix_strings[7].append(0)


    if button8_8._fg_color == "dark red":
        matrix_strings[7].append(1)
    else:
        matrix_strings[7].append(0)

    if button8_9._fg_color == "dark red":
        matrix_strings[7].append(1)
    else:
        matrix_strings[7].append(0)


    if button8_10._fg_color == "dark red":
        matrix_strings[7].append(1)
    else:
        matrix_strings[7].append(0)  






    if button9_1._fg_color == "dark red":
        matrix_strings[8].append(1)
    else:
        matrix_strings[8].append(0)

    if button9_2._fg_color == "dark red":
        matrix_strings[8].append(1)
    else:
        matrix_strings[8].append(0)



    if button9_3._fg_color == "dark red":
        matrix_strings[8].append(1)
    else:
        matrix_strings[8].append(0)


    if button9_4._fg_color == "dark red":
        matrix_strings[8].append(1)
    else:
        matrix_strings[8].append(0)

    if button9_5._fg_color == "dark red":
        matrix_strings[8].append(1)
    else:
        matrix_strings[8].append(0)


    if button9_6._fg_color == "dark red":
        matrix_strings[8].append(1)
    else:
        matrix_strings[8].append(0)  

    if button9_7._fg_color == "dark red":
        matrix_strings[8].append(1)
    else:
        matrix_strings[8].append(0)


    if button9_8._fg_color == "dark red":
        matrix_strings[8].append(1)
    else:
        matrix_strings[8].append(0)

    if button9_9._fg_color == "dark red":
        matrix_strings[8].append(1)
    else:
        matrix_strings[8].append(0)


    if button9_10._fg_color == "dark red":
        matrix_strings[8].append(1)
    else:
        matrix_strings[8].append(0)  







    if button10_1._fg_color == "dark red":
        matrix_strings[9].append(1)
    else:
        matrix_strings[9].append(0)

    if button10_2._fg_color == "dark red":
        matrix_strings[9].append(1)
    else:
        matrix_strings[9].append(0)



    if button10_3._fg_color == "dark red":
        matrix_strings[9].append(1)
    else:
        matrix_strings[9].append(0)


    if button10_4._fg_color == "dark red":
        matrix_strings[9].append(1)
    else:
        matrix_strings[9].append(0)

    if button10_5._fg_color == "dark red":
        matrix_strings[9].append(1)
    else:
        matrix_strings[9].append(0)


    if button10_6._fg_color == "dark red":
        matrix_strings[9].append(1)
    else:
        matrix_strings[9].append(0)  

    if button10_7._fg_color == "dark red":
        matrix_strings[9].append(1)
    else:
        matrix_strings[9].append(0)


    if button10_8._fg_color == "dark red":
        matrix_strings[9].append(1)
    else:
        matrix_strings[9].append(0)

    if button10_9._fg_color == "dark red":
        matrix_strings[9].append(1)
    else:
        matrix_strings[9].append(0)


    if button10_10._fg_color == "dark red":
        matrix_strings[9].append(1)
    else:
        matrix_strings[9].append(0)  








    if button1_1._fg_color == "dark red":
        matrix_columns[0].append(1)
    else:
        matrix_columns[0].append(0)

    if button2_1._fg_color == "dark red":
        matrix_columns[0].append(1)
    else:
        matrix_columns[0].append(0)



    if button3_1._fg_color == "dark red":
        matrix_columns[0].append(1)
    else:
        matrix_columns[0].append(0)


    if button4_1._fg_color == "dark red":
        matrix_columns[0].append(1)
    else:
        matrix_columns[0].append(0)

    if button5_1._fg_color == "dark red":
        matrix_columns[0].append(1)
    else:
        matrix_columns[0].append(0)


    if button6_1._fg_color == "dark red":
        matrix_columns[0].append(1)
    else:
        matrix_columns[0].append(0)  

    if button7_1._fg_color == "dark red":
        matrix_columns[0].append(1)
    else:
        matrix_columns[0].append(0)


    if button8_1._fg_color == "dark red":
        matrix_columns[0].append(1)
    else:
        matrix_columns[0].append(0)

    if button9_1._fg_color == "dark red":
        matrix_columns[0].append(1)
    else:
        matrix_columns[0].append(0)

    if button10_1._fg_color == "dark red":
        matrix_columns[0].append(1)
    else:
        matrix_columns[0].append(0)  




    if button1_2._fg_color == "dark red":
        matrix_columns[1].append(1)
    else:
        matrix_columns[1].append(0)

    if button2_2._fg_color == "dark red":
        matrix_columns[1].append(1)
    else:
        matrix_columns[1].append(0)



    if button3_2._fg_color == "dark red":
        matrix_columns[1].append(1)
    else:
        matrix_columns[1].append(0)


    if button4_2._fg_color == "dark red":
        matrix_columns[1].append(1)
    else:
        matrix_columns[1].append(0)

    if button5_2._fg_color == "dark red":
        matrix_columns[1].append(1)
    else:
        matrix_columns[1].append(0)


    if button6_2._fg_color == "dark red":
        matrix_columns[1].append(1)
    else:
        matrix_columns[1].append(0)  

    if button7_2._fg_color == "dark red":
        matrix_columns[1].append(1)
    else:
        matrix_columns[1].append(0)


    if button8_2._fg_color == "dark red":
        matrix_columns[1].append(1)
    else:
        matrix_columns[1].append(0)

    if button9_2._fg_color == "dark red":
        matrix_columns[1].append(1)
    else:
        matrix_columns[1].append(0)

    if button10_2._fg_color == "dark red":
        matrix_columns[1].append(1)
    else:
        matrix_columns[1].append(0)  




    if button1_3._fg_color == "dark red":
        matrix_columns[2].append(1)
    else:
        matrix_columns[2].append(0)

    if button2_3._fg_color == "dark red":
        matrix_columns[2].append(1)
    else:
        matrix_columns[2].append(0)



    if button3_3._fg_color == "dark red":
        matrix_columns[2].append(1)
    else:
        matrix_columns[2].append(0)


    if button4_3._fg_color == "dark red":
        matrix_columns[2].append(1)
    else:
        matrix_columns[2].append(0)

    if button5_3._fg_color == "dark red":
        matrix_columns[2].append(1)
    else:
        matrix_columns[2].append(0)


    if button6_3._fg_color == "dark red":
        matrix_columns[2].append(1)
    else:
        matrix_columns[2].append(0)  

    if button7_3._fg_color == "dark red":
        matrix_columns[2].append(1)
    else:
        matrix_columns[2].append(0)


    if button8_3._fg_color == "dark red":
        matrix_columns[2].append(1)
    else:
        matrix_columns[2].append(0)

    if button9_3._fg_color == "dark red":
        matrix_columns[2].append(1)
    else:
        matrix_columns[2].append(0)

    if button10_3._fg_color == "dark red":
        matrix_columns[2].append(1)
    else:
        matrix_columns[2].append(0)  







    if button1_4._fg_color == "dark red":
        matrix_columns[3].append(1)
    else:
        matrix_columns[3].append(0)

    if button2_4._fg_color == "dark red":
        matrix_columns[3].append(1)
    else:
        matrix_columns[3].append(0)



    if button3_4._fg_color == "dark red":
        matrix_columns[3].append(1)
    else:
        matrix_columns[3].append(0)


    if button4_4._fg_color == "dark red":
        matrix_columns[3].append(1)
    else:
        matrix_columns[3].append(0)

    if button5_4._fg_color == "dark red":
        matrix_columns[3].append(1)
    else:
        matrix_columns[3].append(0)


    if button6_4._fg_color == "dark red":
        matrix_columns[3].append(1)
    else:
        matrix_columns[3].append(0)  

    if button7_4._fg_color == "dark red":
        matrix_columns[3].append(1)
    else:
        matrix_columns[3].append(0)


    if button8_4._fg_color == "dark red":
        matrix_columns[3].append(1)
    else:
        matrix_columns[3].append(0)

    if button9_4._fg_color == "dark red":
        matrix_columns[3].append(1)
    else:
        matrix_columns[3].append(0)

    if button10_4._fg_color == "dark red":
        matrix_columns[3].append(1)
    else:
        matrix_columns[3].append(0)  





    if button1_5._fg_color == "dark red":
        matrix_columns[4].append(1)
    else:
        matrix_columns[4].append(0)

    if button2_5._fg_color == "dark red":
        matrix_columns[4].append(1)
    else:
        matrix_columns[4].append(0)



    if button3_5._fg_color == "dark red":
        matrix_columns[4].append(1)
    else:
        matrix_columns[4].append(0)


    if button4_5._fg_color == "dark red":
        matrix_columns[4].append(1)
    else:
        matrix_columns[4].append(0)

    if button5_5._fg_color == "dark red":
        matrix_columns[4].append(1)
    else:
        matrix_columns[4].append(0)


    if button6_5._fg_color == "dark red":
        matrix_columns[4].append(1)
    else:
        matrix_columns[4].append(0)  

    if button7_5._fg_color == "dark red":
        matrix_columns[4].append(1)
    else:
        matrix_columns[4].append(0)


    if button8_5._fg_color == "dark red":
        matrix_columns[4].append(1)
    else:
        matrix_columns[4].append(0)

    if button9_5._fg_color == "dark red":
        matrix_columns[4].append(1)
    else:
        matrix_columns[4].append(0)

    if button10_5._fg_color == "dark red":
        matrix_columns[4].append(1)
    else:
        matrix_columns[4].append(0)  





    if button1_6._fg_color == "dark red":
        matrix_columns[5].append(1)
    else:
        matrix_columns[5].append(0)

    if button2_6._fg_color == "dark red":
        matrix_columns[5].append(1)
    else:
        matrix_columns[5].append(0)



    if button3_6._fg_color == "dark red":
        matrix_columns[5].append(1)
    else:
        matrix_columns[5].append(0)


    if button4_6._fg_color == "dark red":
        matrix_columns[5].append(1)
    else:
        matrix_columns[5].append(0)

    if button5_6._fg_color == "dark red":
        matrix_columns[5].append(1)
    else:
        matrix_columns[5].append(0)


    if button6_6._fg_color == "dark red":
        matrix_columns[5].append(1)
    else:
        matrix_columns[5].append(0)  

    if button7_6._fg_color == "dark red":
        matrix_columns[5].append(1)
    else:
        matrix_columns[5].append(0)


    if button8_6._fg_color == "dark red":
        matrix_columns[5].append(1)
    else:
        matrix_columns[5].append(0)

    if button9_6._fg_color == "dark red":
        matrix_columns[5].append(1)
    else:
        matrix_columns[5].append(0)

    if button10_6._fg_color == "dark red":
        matrix_columns[5].append(1)
    else:
        matrix_columns[5].append(0)  







    if button1_7._fg_color == "dark red":
        matrix_columns[6].append(1)
    else:
        matrix_columns[6].append(0)

    if button2_7._fg_color == "dark red":
        matrix_columns[6].append(1)
    else:
        matrix_columns[6].append(0)



    if button3_7._fg_color == "dark red":
        matrix_columns[6].append(1)
    else:
        matrix_columns[6].append(0)


    if button4_7._fg_color == "dark red":
        matrix_columns[6].append(1)
    else:
        matrix_columns[6].append(0)

    if button5_7._fg_color == "dark red":
        matrix_columns[6].append(1)
    else:
        matrix_columns[6].append(0)


    if button6_7._fg_color == "dark red":
        matrix_columns[6].append(1)
    else:
        matrix_columns[6].append(0)  

    if button7_7._fg_color == "dark red":
        matrix_columns[6].append(1)
    else:
        matrix_columns[6].append(0)


    if button8_7._fg_color == "dark red":
        matrix_columns[6].append(1)
    else:
        matrix_columns[6].append(0)

    if button9_7._fg_color == "dark red":
        matrix_columns[6].append(1)
    else:
        matrix_columns[6].append(0)

    if button10_7._fg_color == "dark red":
        matrix_columns[6].append(1)
    else:
        matrix_columns[6].append(0)  







    if button1_8._fg_color == "dark red":
        matrix_columns[7].append(1)
    else:
        matrix_columns[7].append(0)

    if button2_8._fg_color == "dark red":
        matrix_columns[7].append(1)
    else:
        matrix_columns[7].append(0)



    if button3_8._fg_color == "dark red":
        matrix_columns[7].append(1)
    else:
        matrix_columns[7].append(0)


    if button4_8._fg_color == "dark red":
        matrix_columns[7].append(1)
    else:
        matrix_columns[7].append(0)

    if button5_8._fg_color == "dark red":
        matrix_columns[7].append(1)
    else:
        matrix_columns[7].append(0)


    if button6_8._fg_color == "dark red":
        matrix_columns[7].append(1)
    else:
        matrix_columns[7].append(0)  

    if button7_8._fg_color == "dark red":
        matrix_columns[7].append(1)
    else:
        matrix_columns[7].append(0)


    if button8_8._fg_color == "dark red":
        matrix_columns[7].append(1)
    else:
        matrix_columns[7].append(0)

    if button9_8._fg_color == "dark red":
        matrix_columns[7].append(1)
    else:
        matrix_columns[7].append(0)

    if button10_8._fg_color == "dark red":
        matrix_columns[7].append(1)
    else:
        matrix_columns[7].append(0)  





    if button1_9._fg_color == "dark red":
        matrix_columns[8].append(1)
    else:
        matrix_columns[8].append(0)

    if button2_9._fg_color == "dark red":
        matrix_columns[8].append(1)
    else:
        matrix_columns[8].append(0)



    if button3_9._fg_color == "dark red":
        matrix_columns[8].append(1)
    else:
        matrix_columns[8].append(0)


    if button4_9._fg_color == "dark red":
        matrix_columns[8].append(1)
    else:
        matrix_columns[8].append(0)

    if button5_9._fg_color == "dark red":
        matrix_columns[8].append(1)
    else:
        matrix_columns[8].append(0)


    if button6_9._fg_color == "dark red":
        matrix_columns[8].append(1)
    else:
        matrix_columns[8].append(0)  

    if button7_9._fg_color == "dark red":
        matrix_columns[8].append(1)
    else:
        matrix_columns[8].append(0)


    if button8_9._fg_color == "dark red":
        matrix_columns[8].append(1)
    else:
        matrix_columns[8].append(0)

    if button9_9._fg_color == "dark red":
        matrix_columns[8].append(1)
    else:
        matrix_columns[8].append(0)

    if button10_9._fg_color == "dark red":
        matrix_columns[8].append(1)
    else:
        matrix_columns[8].append(0)  







    if button1_10._fg_color == "dark red":
        matrix_columns[9].append(1)
    else:
        matrix_columns[9].append(0)

    if button2_10._fg_color == "dark red":
        matrix_columns[9].append(1)
    else:
        matrix_columns[9].append(0)



    if button3_10._fg_color == "dark red":
        matrix_columns[9].append(1)
    else:
        matrix_columns[9].append(0)


    if button4_10._fg_color == "dark red":
        matrix_columns[9].append(1)
    else:
        matrix_columns[9].append(0)

    if button5_10._fg_color == "dark red":
        matrix_columns[9].append(1)
    else:
        matrix_columns[9].append(0)


    if button6_10._fg_color == "dark red":
        matrix_columns[9].append(1)
    else:
        matrix_columns[9].append(0)  

    if button7_10._fg_color == "dark red":
        matrix_columns[9].append(1)
    else:
        matrix_columns[9].append(0)


    if button8_10._fg_color == "dark red":
        matrix_columns[9].append(1)
    else:
        matrix_columns[9].append(0)

    if button9_10._fg_color == "dark red":
        matrix_columns[9].append(1)
    else:
        matrix_columns[9].append(0)

    if button10_10._fg_color == "dark red":
        matrix_columns[9].append(1)
    else:
        matrix_columns[9].append(0)  

        


    count1 = 0
    column_count1 = 0

    counter_cells1 = []

    counter_cells = []

    column_count = 0

    count = 0

    for string in matrix_strings:
        for cell in string:
            for index in range(5):
                try:
                    counter_cells1.append(string[count1 + index])
                except:
                    counter_cells1.append(1)

            if 1 in counter_cells1:
                pass
            elif 1 not in counter_cells1:
                for index in range(5):
                    try:
                        final_matrix[column_count1][count1 + index] += 1
                    except:
                        counter_cells1.append(1)
            count1 += 1
            counter_cells1 = []
        count1 = 0
        column_count1 += 1


                
    for column in matrix_columns:
        for cell in column:
            for index in range(5):
                try:
                    counter_cells.append(column[count + index])
                except:
                    counter_cells.append(1)

            if 1 in counter_cells:
                pass
            elif 1 not in counter_cells:
                for index in range(5):
                    try:
                        final_matrix[count + index][column_count] += 1
                    except:
                        counter_cells.append(1)
            count += 1
            counter_cells = []
        count = 0
        column_count += 1
        
        


    
    count1 = 0

    column_count1 = 0

    counter_cells1 = []

    counter_cells = []

    column_count = 0

    count = 0

    for string in matrix_strings:
        for cell in string:
            for index in range(4):
                try:
                    counter_cells1.append(string[count1 + index])
                except:
                    counter_cells1.append(1)

            if 1 in counter_cells1:
                pass
            elif 1 not in counter_cells1:
                for index in range(4):
                    try:
                        final_matrix[column_count1][count1 + index] += 1
                    except:
                        counter_cells1.append(1)
            count1 += 1
            counter_cells1 = []
        count1 = 0
        column_count1 += 1

        
                
    for column in matrix_columns:
        for cell in column:
            for index in range(4):
                try:
                    counter_cells.append(column[count + index])
                except:
                    counter_cells.append(1)

            if 1 in counter_cells:
                pass
            elif 1 not in counter_cells:
                for index in range(4):
                    try:
                        final_matrix[count + index][column_count] += 1
                    except:
                        counter_cells.append(1)
            count += 1
            counter_cells = []
        count = 0
        column_count += 1
                
        



    
    count1 = 0

    column_count1 = 0

    counter_cells1 = []

    counter_cells = []

    column_count = 0

    count = 0

    for string in matrix_strings:
        for cell in string:
            for index in range(3):
                try:
                    counter_cells1.append(string[count1 + index])
                except:
                    counter_cells1.append(1)

            if 1 in counter_cells1:
                pass
            elif 1 not in counter_cells1:
                for index in range(3):
                    try:
                        final_matrix[column_count1][count1 + index] += 1
                    except:
                        counter_cells1.append(1)
            count1 += 1
            counter_cells1 = []
        count1 = 0
        column_count1 += 1

        
                
    for column in matrix_columns:
        for cell in column:
            for index in range(3):
                try:
                    counter_cells.append(column[count + index])
                except:
                    counter_cells.append(1)

            if 1 in counter_cells:
                pass
            elif 1 not in counter_cells:
                for index in range(3):
                    try:
                        final_matrix[count + index][column_count] += 1
                    except:
                        counter_cells.append(1)
            count += 1
            counter_cells = []
        count = 0
        column_count += 1
        
    
    

                
        


    
    count1 = 0

    column_count1 = 0

    counter_cells1 = []

    counter_cells = []

    column_count = 0

    count = 0

    for string in matrix_strings:
        for cell in string:
            for index in range(2):
                try:
                    counter_cells1.append(string[count1 + index])
                except:
                    counter_cells1.append(1)

            if 1 in counter_cells1:
                pass
            elif 1 not in counter_cells1:
                for index in range(2):
                    try:
                        final_matrix[column_count1][count1 + index] += 2
                    except:
                        counter_cells1.append(1)
            count1 += 1
            counter_cells1 = []
        count1 = 0
        column_count1 += 1

            
                
    for column in matrix_columns:
        for cell in column:
            for index in range(2):
                try:
                    counter_cells.append(column[count + index])
                except:
                    counter_cells.append(1)

            if 1 in counter_cells:
                pass
            elif 1 not in counter_cells:
                for index in range(2):
                    try:
                        final_matrix[count + index][column_count] += 2
                    except:
                        counter_cells.append(1)
            count += 1
            counter_cells = []
        count = 0
        column_count += 1

            
    print("\n\nstrings:\n")
    for string in matrix_strings:
        print(string)


    print("\n\ncolumns:\n")
    for column in matrix_columns:
        print(column)

    print("\n\n", matrix_cells)
    for cell in matrix_cells:
        print(cell)


    for string in final_matrix:
        print(f"sosiska {string}")


    max_value = float('-inf')
    max_index = (-1, -1)


    for i in range(len(final_matrix)):
        for j in range(len(final_matrix[i])):
            if final_matrix[i][j] > max_value:
                max_value = final_matrix[i][j]
                max_index = (i, j)

    print("Наибольшее число в матрице:", max_value)
    print("Индекс наибольшего числа в матрице:", max_index)

                

    



    button_dict[f"button{max_index[0] + 1}_{max_index[1] + 1}"].configure(fg_color = "dark green")      





    final_matrix = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],  
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
    ]




button_submit = customtkinter.CTkButton(screen, text="SUMBIT", font=(25,25), width= 200, height= 50, border_width= 2, border_color= "black", corner_radius= 10, fg_color= "grey", text_color="black", command= sumbit_cmd)




letters.place(x = 115, y = 70)

numbers.place(x = 70, y = 100)
numbers2.place(x = 70, y = 255)
numbers3.place(x = 70, y = 405)
numbers4.place(x = 65, y = 555)




for btn in list_btns:
    btn.place(x = count1, y = count2)
    count1 += 49
    if count_cells % 10 == 0:
        count1 = 100
        count2 += 49
    count_cells += 1

clear_button.place(x = 650, y = 0)

notes_button.place(x = 650, y = 50)

button_submit.place(x = 250, y = 600)


screen.mainloop()