questions = [["What is the chemical symbol for hydrogen?", "a. H", "b. C", "c. N", "d. O", "a"],
             ["What is the smallest unit of matter?", "a) Cell", "b) Molecule", "c) Atom", "d) Nucleus", "c"],
             ["Which planet is closest to the Sun?", "a) Mercury", "b) Venus", "c) Mars", "d) Jupiter", "a"],
             ["What is the process by which plants convert sunlight into energy?", "a) Respiration",
              "b) Photosynthesis", "c) Transpiration", "d) Germination", "b"],
             ["What is the study of fossils called?", "a) Archaeology", "b) Anthropology", "c) Paleontology",
              "d) Geology", "c"]]

prize = [1000, 2000, 3000, 5000]

for i in range(len(questions)):
    print(questions[i][0])
    print(questions[i][1], "          ", questions[i][2])
    print(questions[i][3], "          ", questions[i][4])
    a = input("\nIf you want to use a lifeline, press 3: ")

    if a == "3":
        x = questions[i][-1]
        y = len(questions[i])
        z = i
        for j in range(y - 1, 0, -1):
            if x != questions[i][j]:
                questions[i].pop(j)

    if a == questions[i][-1]:
        print("You are correct!")
    else:
        print("You are incorrect!")
        break
