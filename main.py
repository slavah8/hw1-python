courselettergrade1=str(input("Enter your course 1 letter grade: "));
coursecredit1=int(input("Enter your course 1 credit: "));

if courselettergrade1 == "A" or courselettergrade1 == "a":
   gradepoint1 = 4.0;
   
elif courselettergrade1 =="A-" or courselettergrade1 == "a-":
  gradepoint1 = 3.67;

elif courselettergrade1 == "B+" or courselettergrade1 == "b+":
  gradepoint1 = 3.33;

elif courselettergrade1 == "B" or courselettergrade1 == "b":
  gradepoint1 = 3.0;

elif courselettergrade1 == "B-" or courselettergrade1 == "b-":
  gradepoint1 = 2.67;

elif courselettergrade1 == "C+" or courselettergrade1 == "c+":
  gradepoint1 = 2.33;

elif courselettergrade1 == "C" or courselettergrade1 == "c":
  gradepoint1 = 2.0;

elif courselettergrade1 == "D" or courselettergrade1 == "d":
  gradepoint1 = 1.0;

else:
  gradepoint1 = 0;

print(f"Grade point for course 1 is: {gradepoint1}");


courselettergrade2=str(input("Enter your course 2 letter grade: "));
coursecredit2=int(input("Enter your course 2 credit: "));

if courselettergrade2 == "A" or courselettergrade2 == "a":
   gradepoint2 = 4.0;
   
elif courselettergrade2 =="A-" or courselettergrade2 == "a-":
  gradepoint2 = 3.67;

elif courselettergrade2 == "B+" or courselettergrade2 == "b+":
  gradepoint2 = 3.33;

elif courselettergrade2 == "B" or courselettergrade2 == "b":
  gradepoint2 = 3.0;

elif courselettergrade2 == "B-" or courselettergrade2 == "b-":
  gradepoint2 = 2.67;

elif courselettergrade2 == "C+" or courselettergrade2 == "c+":
  gradepoint2 = 2.33;

elif courselettergrade2 == "C" or courselettergrade2 == "c":
  gradepoint2 = 2.0;

elif courselettergrade2 == "D" or courselettergrade2 == "d":
  gradepoint2 = 1.0;

else:
  gradepoint2 = 0;

print(f"Grade point for course 2 is: {gradepoint2}");

courselettergrade3=str(input("Enter your course 3 letter grade: "));
coursecredit3=int(input("Enter your course 3 credit: "));

if courselettergrade3 == "A" or courselettergrade3 == "a":
   gradepoint3 = 4.0;
   
elif courselettergrade3 =="A-" or courselettergrade3 == "a-":
  gradepoint3 = 3.67;

elif courselettergrade3 == "B+" or courselettergrade3 == "b+":
  gradepoint3 = 3.33;

elif courselettergrade3 == "B" or courselettergrade3 == "b":
  gradepoint3 = 3.0;

elif courselettergrade3 == "B-" or courselettergrade3 == "b-":
  gradepoint3 = 2.67;

elif courselettergrade3 == "C+" or courselettergrade3 == "c+":
  gradepoint3 = 2.33;

elif courselettergrade3 == "C" or courselettergrade3 == "c":
  gradepoint3 = 2.0;

elif courselettergrade3 == "D" or courselettergrade3 == "d":
  gradepoint3 = 1.0;

else:
  gradepoint3 = 0;

print(f"Grade point for course 1 is: {gradepoint3}");

GPA = (gradepoint1 * coursecredit1 + gradepoint2 * coursecredit2 + gradepoint3 * coursecredit3) / (coursecredit1 + coursecredit2 + coursecredit3) 
print(f"Your GPA is: {GPA}");
