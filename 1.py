from colorama import init
init()
from colorama import Fore, Back, Style
import numpy as np

print(Fore.CYAN)
print(Back.BLACK)
print(Style.BRIGHT)

print('Определите, какой тип темперамента по Гиппо-\n'
'крату – холерик, сангвиник, флегматик или меланхолик, – представлен у вас ярче всего.\n'
'Вспомним, что чистых темпераментов не существует – как правило,\n'
'один или два выражены у человека больше, остальные – меньше.\n'
'Люди, у которых все типы темпераментов представлены примерно по 25%, называются тетравертами.\n')
print(Fore.RED)
print(Back.BLACK)
print(Style.BRIGHT)
print('Инструкция к тесту\n'
'Тест состоит из 80 вопросов, на которые вам предлагается ответить "+" или "-".\n'
'Выберете, какие утверждения для вас характерны, а какие нет.\n'
'Помните, что правильных и неправильных ответов здесь нет. Отвечать нужно быстро, не задумываясь.')



print(Fore.MAGENTA)
print(Back.BLACK)
print(Style.BRIGHT)

q1_1 = str(input("1. неусидчивы, суетливы;	"))
q2_1 = str(input("2. невыдержанны, вспыльчивы;	"))
q3_1 = str(input("3. нетерпеливы; "))
q4_1 = str(input("4. резки и прямолинейны в отношениях с людьми;	"))
q5_1 = str(input("5. решительны и инициативны;	"))
q6_1 = str(input("6. упрямы;	"))
q7_1 = str(input("7. находчивы в споре;	"))
q8_1 = str(input("8. работаете рывками;	"))
q9_1 = str(input("9. склонны к риску;	"))
q10_1 = str(input("10. незлопамятны;	"))
q11_1 = str(input("11. обладаете быстрой, страстной, со сбивчивыми интонациями речью;	"))
q12_1 = str(input("12. неуравновешенны и склонны к горячности;	"))
q13_1 = str(input("13. агрессивный забияка;	"))
q14_1 = str(input("14. нетерпимы к недостаткам;	"))
q15_1 = str(input("15. обладаете выразительной мимикой;	"))
q16_1 = str(input("16. способны быстро действовать и решать;	"))
q17_1 = str(input("17. неустанно стремитесь к новому;	"))
q18_1 = str(input("18. обладаете резкими порывистыми движениями;	"))
q19_1 = str(input("19. настойчивы в достижении поставленной цели;	"))
q20_1 = str(input("20. склонны к резким сменам настроения	"))
q1_2 = str(input("21. веселы и жизнерадостны;"))
q2_2 = str(input("22. энергичны и деловиты;"))
q3_2 = str(input("23. часто не доводите начатое дело до конца;"))
q4_2 = str(input("24. склонны переоценивать себя;"))
q5_2 = str(input("25. способны быстро схватывать новое;"))
q6_2 = str(input("26. неустойчивы в интересах и склонностях;"))
q7_2 = str(input("27. легко переживаете неудачи и неприятности;"))
q8_2 = str(input("28. легко приспосабливаетесь к разным обстоятельствам;"))
q9_2 = str(input("29. с увлечением беретесь за любое новое дело;"))
q10_2 = str(input("30. быстро остываете, если дело перестает вас интересовать;"))
q11_2 = str(input("31. быстро включаетесь в новую работу и быстро переключаетесь с одной работы на другую;"))
q12_2 = str(input("32. тяготитесь однообразием будничной кропотливой работы;"))
q13_2 = str(input("33. общительны и отзывчивы, не чувствуете скованности с новыми для вас людьми;"))
q14_2 = str(input("34. выносливы и работоспособны;"))
q15_2 = str(input("35. обладаете громкой, быстрой, отчетливой речью, \n"
"4сопровождающейся жестами, выразительной мимикой;"))
q16_2 = str(input("36. сохраняете самообладание в неожиданной сложной обстановке;"))
q17_2 = str(input("37. обладаете всегда бодрым настроением;"))
q18_2 = str(input("38. быстро засыпаете и пробуждаетесь;"))
q19_2 = str(input("39. часто не собраны, проявляете поспешность в решениях;"))
q20_2 = str(input("40. склонны иногда скользить по поверхности, отвлекаться;"))
q1_3 = str(input("41. веселы и жизнерадостны;"))
q2_3 = str(input("42. энергичны и деловиты;"))
q3_3 = str(input("43. часто не доводите начатое дело до конца;"))
q4_3 = str(input("44. склонны переоценивать себя;"))
q5_3 = str(input("45. способны быстро схватывать новое;"))
q6_3 = str(input("46. неустойчивы в интересах и склонностях;"))
q7_3 = str(input("47. легко переживаете неудачи и неприятности;"))
q8_3 = str(input("48. легко приспосабливаетесь к разным обстоятельствам;"))
q9_3 = str(input("49. с увлечением беретесь за любое новое дело;"))
q10_3 = str(input("50. быстро остываете, если дело перестает вас интересовать;"))
q11_3 = str(input("51. быстро включаетесь в новую работу и быстро переключаетесь с одной работы на другую;"))
q12_3 = str(input("52. тяготитесь однообразием будничной кропотливой работы;"))
q13_3 = str(input("53. общительны и отзывчивы, не чувствуете скованности с новыми для вас людьми;"))
q14_3 = str(input("54. выносливы и работоспособны;"))
q15_3 = str(input("55. обладаете громкой, быстрой, отчетливой речью, сопровождающейся жестами, выразительной мимикой;"))
q16_3 = str(input("56. сохраняете самообладание в неожиданной сложной обстановке;"))
q17_3 = str(input("57. обладаете всегда бодрым настроением;"))
q18_3 = str(input("58. быстро засыпаете и пробуждаетесь;"))
q19_3 = str(input("59. часто не собраны, проявляете поспешность в решениях;"))
q20_3 = str(input("60. склонны иногда скользить по поверхности, отвлекаться"))
q1_4 = str(input("61. стеснительны и застенчивы;"))
q2_4 = str(input("62. теряетесь в новой обстановке;"))
q3_4 = str(input("63. затрудняетесь установить контакт с незнакомыми людьми;"))
q4_4 = str(input("64. не верите в свои силы;"))
q5_4 = str(input("65. легко переносите одиночество;"))
q6_4 = str(input("66.чувствуете подавленность и растерянность при неудачах;"))
q7_4 = str(input("67. склонны уходить в себя;"))
q8_4 = str(input("68. быстро утомляетесь;"))
q9_4 = str(input("69. обладаете тихой речью;"))
q10_4 = str(input("70. невольно приспосабливаетесь к характеру собеседника;"))
q11_4 = str(input("71. впечатлительны до слезливости;"))
q12_4 = str(input("72. чрезвычайно восприимчивы к одобрению и порицанию;"))
q13_4 = str(input("73. предъявляете высокие требования к себе и окружающим;"))
q14_4 = str(input("74. склонны к подозрительности, мнительности;"))
q15_4 = str(input("75. болезненно чувствительны и легко ранимы;"))
q16_4 = str(input("76. чрезмерно обидчивы;"))
q17_4 = str(input("77. скрытны и необщительны, не делитесь ни с кем своими мыслями;"))
q18_4 = str(input("78. малоактивны и робки;"))
q19_4 = str(input("79. уступчивы, покорны;"))
q20_4 = str(input("80. стремитесь вызвать сочувствие и помощь у окружающих"))



print(Fore.RED)
print(Back.BLACK)
print(Style.BRIGHT)

if q1_1 == "+":
	q1_1 = 1
elif q1_1 == "-":
	q1_1 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q2_1 == "+":
	q2_1 = 1
elif q2_1 == "-":
	q2_1 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q3_1 == "+":
	q3_1 = 1
elif q3_1 == "-":
	q3_1 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q4_1 == "+":
	q4_1 = 1
elif q4_1 == "-":
	q4_1 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q5_1 == "+":
	q5_1 = 1
elif q5_1 == "-":
	q5_1 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q6_1 == "+":
	q6_1 = 1
elif q6_1 == "-":
	q6_1 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q7_1 == "+":
	q7_1 = 1
elif q7_1 == "-":
	q7_1 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q8_1 == "+":
	q8_1 = 1
elif q8_1 == "-":
	q8_1 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q9_1 == "+":
	q9_1 = 1
elif q9_1 == "-":
	q9_1 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q10_1 == "+":
	q10_1 = 1
elif q10_1 == "-":
	q10_1 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q11_1 == "+":
	q11_1 = 1
elif q11_1 == "-":
	q11_1 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q12_1 == "+":
	q12_1 = 1
elif q12_1 == "-":
	q12_1 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q13_1 == "+":
	q13_1 = 1
elif q13_1 == "-":
	q13_1 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q14_1 == "+":
	q14_1 = 1
elif q14_1 == "-":
	q14_1 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q15_1 == "+":
	q15_1 = 1
elif q15_1 == "-":
	q15_1 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q16_1 == "+":
	q16_1 = 1
elif q16_1 == "-":
	q16_1 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q17_1 == "+":
	q17_1 = 1
elif q17_1 == "-":
	q17_1 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q18_1 == "+":
	q18_1 = 1
elif q18_1 == "-":
	q18_1 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q19_1 == "+":
	q19_1 = 1
elif q19_1 == "-":
	q19_1 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q20_1 == "+":
	q20_1 = 1
elif q20_1 == "-":
	q20_1 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q1_2 == "+":
	q1_2 = 1
elif q1_2 == "-":
	q1_2 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q2_2 == "+":
	q2_2 = 1
elif q2_2 == "-":
	q2_2 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q3_2 == "+":
	q3_2 = 1
elif q3_2 == "-":
	q3_2 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q4_2 == "+":
	q4_2 = 1
elif q4_2 == "-":
	q4_2 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q5_2 == "+":
	q5_2 = 1
elif q5_2 == "-":
	q5_2 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q6_2 == "+":
	q6_2 = 1
elif q6_2 == "-":
	q6_2 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q7_2 == "+":
	q7_2 = 1
elif q7_2 == "-":
	q7_2 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q8_2 == "+":
	q8_2 = 1
elif q8_2 == "-":
	q8_2 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q9_2 == "+":
	q9_2 = 1
elif q9_2 == "-":
	q9_2 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q10_2 == "+":
	q10_2 = 1
elif q10_2 == "-":
	q10_2 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q11_2 == "+":
	q11_2 = 1
elif q11_2 == "-":
	q11_2 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q12_2 == "+":
	q12_2 = 1
elif q12_2 == "-":
	q12_2 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q13_2 == "+":
	q13_2 = 1
elif q13_2 == "-":
	q13_2 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q14_2 == "+":
	q14_2 = 1
elif q14_2 == "-":
	q14_2 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q15_2 == "+":
	q15_2 = 1
elif q15_2 == "-":
	q15_2 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q16_2 == "+":
	q16_2 = 1
elif q16_2 == "-":
	q16_2 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q17_2 == "+":
	q17_2 = 1
elif q17_2 == "-":
	q17_2 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q18_2 == "+":
	q18_2 = 1
elif q18_2 == "-":
	q18_2 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q19_2 == "+":
	q19_2 = 1
elif q19_2 == "-":
	q19_2 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q20_2 == "+":
	q20_2 = 1
elif q20_2 == "-":
	q20_2 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q1_3 == "+":
	q1_3 = 1
elif q1_3 == "-":
	q1_3 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q2_3 == "+":
	q2_3 = 1
elif q2_3 == "-":
	q2_3 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q3_3 == "+":
	q3_3 = 1
elif q3_3 == "-":
	q3_3 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q4_3 == "+":
	q4_3 = 1
elif q4_3 == "-":
	q4_3 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q5_3 == "+":
	q5_3 = 1
elif q5_3 == "-":
	q5_3 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q6_3 == "+":
	q6_3 = 1
elif q6_3 == "-":
	q6_3 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q7_3 == "+":
	q7_3 = 1
elif q7_3 == "-":
	q7_3 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q8_3 == "+":
	q8_3 = 1
elif q8_3 == "-":
	q8_3 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q9_3 == "+":
	q9_3 = 1
elif q9_3 == "-":
	q9_3 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q10_3 == "+":
	q10_3 = 1
elif q10_3 == "-":
	q10_3 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q11_3 == "+":
	q11_3 = 1
elif q11_3 == "-":
	q11_3 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q12_3 == "+":
	q12_3 = 1
elif q12_3 == "-":
	q12_3 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q13_3 == "+":
	q13_3 = 1
elif q13_3 == "-":
	q13_3 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q14_3 == "+":
	q14_3 = 1
elif q14_3 == "-":
	q14_3 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q15_3 == "+":
	q15_3 = 1
elif q15_3 == "-":
	q15_3 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q16_3 == "+":
	q16_3 = 1
elif q16_3 == "-":
	q16_3 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q17_3 == "+":
	q17_3 = 1
elif q17_3 == "-":
	q17_3 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q18_3 == "+":
	q18_3 = 1
elif q18_3 == "-":
	q18_3 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q19_3 == "+":
	q19_3 = 1
elif q19_3 == "-":
	q19_3 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q20_3 == "+":
	q20_3 = 1
elif q20_3 == "-":
	q20_3 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q1_4 == "+":
	q1_4 = 1
elif q1_4 == "-":
	q1_4 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q2_4 == "+":
	q2_4 = 1
elif q2_4 == "-":
	q2_4 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q3_4 == "+":
	q3_4 = 1
elif q3_4 == "-":
	q3_4 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q4_4 == "+":
	q4_4 = 1
elif q4_4 == "-":
	q4_4 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q5_4 == "+":
	q5_4 = 1
elif q5_4 == "-":
	q5_4 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q6_4 == "+":
	q6_4 = 1
elif q6_4 == "-":
	q6_4 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q7_4 == "+":
	q7_4 = 1
elif q7_4 == "-":
	q7_4 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q8_4 == "+":
	q8_4 = 1
elif q8_4 == "-":
	q8_4 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q9_4 == "+":
	q9_4 = 1
elif q9_4 == "-":
	q9_4 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q10_4 == "+":
	q10_4 = 1
elif q10_4 == "-":
	q10_4 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q11_4 == "+":
	q11_4 = 1
elif q11_4 == "-":
	q11_4 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q12_4 == "+":
	q12_4 = 1
elif q12_4 == "-":
	q12_4 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q13_4 == "+":
	q13_4 = 1
elif q13_4 == "-":
	q13_4 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q14_4 == "+":
	q14_4 = 1
elif q14_4 == "-":
	q14_4 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q15_4 == "+":
	q15_4 = 1
elif q15_4 == "-":
	q15_4 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q16_4 == "+":
	q16_4 = 1
elif q16_4 == "-":
	q16_4 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q17_4 == "+":
	q17_4 = 1
elif q17_4 == "-":
	q17_4 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q18_4 == "+":
	q18_4 = 1
elif q18_4 == "-":
	q18_4 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q19_4 == "+":
	q19_4 = 1
elif q19_4 == "-":
	q19_4 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

if q20_4 == "+":
	q20_4 = 1
elif q20_4 == "-":
	q20_4 = 0
else:
	print("Вы пропустили вопрос, к сожению, придётся начать заново.")

h = [float(q1_1), float(q2_1), float(q3_1), float(q4_1), float(q5_1), float(q6_1), float(q7_1), float(q8_1), float(q9_1), float(q10_1), float(q11_1), float(q12_1), float(q13_1), float(q14_1), float(q15_1), float(q16_1), float(q17_1), float(q18_1), float(q19_1), float(q20_1)]

s = [float(q1_2), float(q2_2), float(q3_2), float(q4_2), float(q5_2), float(q6_2), float(q7_2), float(q8_2), float(q9_2), float(q10_2), float(q11_2), float(q12_2), float(q13_2), float(q14_2), float(q15_2), float(q16_2), float(q17_2), float(q18_2), float(q19_2), float(q20_2)]

f = [float(q1_3), float(q2_3), float(q3_3), float(q4_3), float(q5_3), float(q6_3), float(q7_3), float(q8_3), float(q9_3), float(q10_3), float(q11_3), float(q12_3), float(q13_3), float(q14_3), float(q15_3), float(q16_3), float(q17_3), float(q18_3), float(q19_3), float(q20_3)]

m = [float(q1_4), float(q2_4), float(q3_4), float(q4_4), float(q5_4), float(q6_4), float(q7_4), float(q8_4), float(q9_4), float(q10_4), float(q11_4), float(q12_4), float(q13_4), float(q14_4), float(q15_4), float(q16_4), float(q17_4), float(q18_4), float(q19_4), float(q20_4)]

print(Fore.YELLOW)
print(Back.BLACK)
print(Style.BRIGHT)

##a = np.array(h+s+f+m)

h = sum(h)
s = sum(s)
f = sum(f)
m = sum(m)

a = h + s + f + m

h = h/a*100
s = s/a*100
f = f/a*100
m = m/a*100

print("Поздравляю, вы успешно прошли тест.")
print("Результат в процентах на сколько вы холерик - " + str(h))
print("Результат в процентах на сколько вы сангвиник - " + str(s))
print("Результат в процентах на сколько вы флегматик - " + str(f))
print("Результат в процентах на сколько вы меланхолик  - " + str(m))

v = int (input('Какой темперамент преобладает у вас больше всего? (Указать цифрой) \n 1 Холерик \n 2 сангвиник \n 3 флегматик \n 4 меланхолик \n'))

if v == 1:
    r = "Люди этого темперамента быстры, чрезмерно подвижны, неуравновешенны, возбудимы, все\n"
"психические процессы протекают у них быстро, интенсивно. Преобладание возбуждения над\n"
"торможением, свойственное этому типу нервной деятельности, ярко проявляется в \n"
"несдержанности, порывистости, вспыльчивости, раздражительности холерика. Отсюда и \n"
"выразительная мимика, торопливая речь, резкие жесты, несдержанные движения. Чувства \n"
"человека холерического темперамента сильные, обычно ярко проявляются, быстро возникают; \n "
"настроение иногда резко меняется. Неуравновешенность, свойственная холерику, ярко \n "
"связывается и в его деятельности: он с увеличением и даже страстью берется за дело, показывая \n "
"при этом порывистость и быстроту движений, работает с подъемом, преодолевая трудности. Но у \n "
"человека с холерическим темпераментом запас нервной энергии может быстро истощиться в \n "
"процессе работы и тогда может наступить резкий спад деятельности: подъем и воодушевление \n "
"исчезают, настроение резко падает. В общении с людьми холерик допускает резкость, \n "
"раздражительность, эмоциональную несдержанность, что часто не дает ему возможности \n"
"объективно оценивать поступки людей, и на этой почве он создает конфликтные ситуации в \n"
"коллективе. Излишняя прямолинейность, вспыльчивость, резкость, нетерпимость порой делают \n"
"тяжелым и неприятным пребывание в коллективе таких людей."
p = 'Холерик - '
t = p
if v == 2:
    r = "Сангвиник быстро сходится с людьми, жизнерадостен, легко переключается с одного вида \n"
"деятельности на другой, но не любит однообразной работы. Он легко контролирует свои эмоции, \n"
"быстро осваивается в новой обстановке, активно вступает в контакты с людьми. Его речь громкая, \n"
"быстрая, отчетливая и сопровождается выразительными мимикой и жестами. Но этот \n"
"темперамент характеризуется некоторой двойственностью. Если раздражители быстро меняются, \n"
"все время поддерживается новизна и интерес впечатлений, у сангвиника создается состояние \n"
"активного возбуждения и он проявляет себя как человек деятельный, активный, энергичный. Если \n"
"же воздействия длительны и однообразны, то они не поддерживают состояния активности, \n"
"возбуждения и сангвиник теряет интерес к делу, у него появляется безразличие, скука, вялость. \n"
"У сангвиника быстро возникают чувства радости, горя, привязанности и недоброжелательности, \n"
"но все эти проявления его чувств неустойчивы, не отличаются длительностью и глубиной. Они \n"
"быстро возникают и могут так же быстро исчезнуть или даже замениться противоположными. \n"
"Настроение сангвиника быстро меняется, но, как правило, преобладает хорошее настроение."
l = 'сангвиник - '
t = l
if v == 3:
    r = "Человек этого темперамента медлителен, спокоен, нетороплив, уравновешен. В деятельности \n" 
"проявляет основательность, продуманность, упорство. Он, как правило, доводит начатое до \n "
"конца. Все психические процессы у флегматика протекают как бы замедленно. Чувства \n "
"флегматика внешне выражаются слабо, они обычно невыразительны. Причина этого - \n "
"уравновешенность и слабая подвижность нервных процессов. В отношениях с людьми флегматик \n" 
"всегда ровен, спокоен, в меру общителен, настроение у него устойчивое. Спокойствие человека \n"
"флегматического темперамента проявляется и в отношении его к событиям и явлениям жизни \n"
"флегматика нелегко вывести из себя и задеть эмоционально. У человека флегматического \n "
"темперамента легко выработать выдержку, хладнокровие, спокойствие. Но у флегматика следует \n "
"развивать недостающие ему качества - большую подвижность, активность, не допускать, чтобы он \n "
"проявлял безразличие к деятельности, вялость, инертность, которые очень легко могут \n "
"сформироваться в определенных условиях. Иногда у человека этого темперамента может \n"
"развиться безразличное отношение к труду, к окружающей жизни, к людям и даже к самому себе. "
m = 'флегматик - '
t = m
if v == 4:
	r = "У меланхоликов медленно протекают психические процессы, они с трудом реагируют на \n"
"Сильные раздражители; длительное и сильное напряжение вызывает у людей этого темперамента \n"
"замедленную деятельность, а затем и прекращение ее. В работе меланхолики обычно пассивны, \n "
"часто мало заинтересованы (ведь заинтересованность всегда связана с сильным нервным \n "
"напряжением). Чувства и эмоциональные состояния у людей меланхолического темперамента \n "
"возникают медленно, но отличаются глубиной, большой силой и длительностью; меланхолики \n "
"легко уязвимы, тяжело переносят обиды, огорчения, хотя внешне все эти переживания у них \n "
"выражаются слабо. Представители меланхолического темперамента склонны к замкнутости и \n "
"одиночеству, избегают общения с малознакомыми, новыми людьми, часто смущаются, проявляют \n "
"большую неловкость в новой обстановке. Все новое, необычное вызывает у меланхоликов \n "
"тормозное состояние. Но в привычной и спокойной обстановке люди с таким темпераментом \n "
"чувствуют себя спокойно и работают очень продуктивно. У меланхоликов легко развивать и \n "
"совершенствовать свойственную им глубину и устойчивость чувств, повышенную \n "
"восприимчивость к внешним воздействиям."
n = 'меланхолик -'
t = n
print ('В кратце  ',t,' = ',r)

input()