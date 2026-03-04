Define a dictionary to store student information

DECLARE students AS DICTIONARY OF STRING * FLOAT
students = {
"Ayse": 78,
"Mehmet": 65,
"Zeynep": 92,
"Can": 55,
"Elif": 80,
"Ali": 73,
"Deniz": 88,
"Ece": 60,
"Kerem": 49,
"Seda": 95,
}

Function to determine letter grade

FUNCTION letter(score: FLOAT) RETURNS STRING
IF score < 0 OR score > 100 THEN
RETURN "INVALID"
ELSE IF score >= 90 THEN
RETURN "A"
ELSE IF score >= 80 THEN
RETURN "B"
ELSE IF score >= 70 THEN
RETURN "C"
ELSE IF score >= 60 THEN
RETURN "D"
ELSE
RETURN "F"
END FUNCTION

Function to add or update student information

FUNCTION add_or_update(name: STRING, score: FLOAT) RETURNS BOOLEAN
IF name IS EMPTY OR score < 0 OR score > 100 THEN
RETURN FALSE
ELSE
students[name] = score
RETURN TRUE
END FUNCTION

Function to calculate summary statistics

FUNCTION summary() RETURNS TUPLE[FLOAT,_INTEGER,_STRING]
DECLARE total AS FLOAT = 0.0
DECLARE best_name AS STRING = NULL
DECLARE best_score AS FLOAT = -1.0

FOR EACH student IN students
    total = total + student.score
    IF student.score > best_score THEN
        best_score = student.score
        best_name = student.name

DECLARE avg AS FLOAT = total / LENGTH(students) IF students ELSE 0.0
RETURN (avg, LENGTH(students), best_name IF best_name ELSE "-")

END FUNCTION

Function to list students above a threshold

FUNCTION list_above(threshold: FLOAT) RETURNS LIST[STRING]
DECLARE names AS LIST[STRING] = EMPTY LIST

FOR EACH student IN students
    IF student.score >= threshold THEN
        APPEND student.name TO names

RETURN names

END FUNCTION

Main program loop

WHILE TRUE
PRINT "\n1) Harf notu sor 2) Ekle/Güncelle 3) Özet 4) 80+ Liste 5) Çıkış"
DECLARE choice AS STRING = INPUT("Seçim: ").strip()

IF choice = "1" THEN
    DECLARE name AS STRING = INPUT("İsim: ").strip()
    IF name NOT IN students THEN
        PRINT "Yok."
    ELSE
        DECLARE sc AS FLOAT = students[name]
        PRINT name + " -> " + sc + " -> " + letter(sc)

ELSE IF choice = "2" THEN
    DECLARE name AS STRING = INPUT("İsim: ").strip()
    DECLARE score_text AS STRING = INPUT("Puan (0-100): ").strip()
    TRY
        DECLARE sc AS FLOAT = CONVERT(score_text TO FLOAT)
    EXCEPT VALUE_ERROR
        PRINT "Puan sayı olmalı."
        CONTINUE

    DECLARE ok AS BOOLEAN = add_or_update(name, sc)
    PRINT "Kaydedildi." IF ok ELSE "Hatalı giriş."

ELSE IF choice = "3" THEN
    DECLARE avg AS FLOAT, count AS INTEGER, best AS STRING
    (avg, count, best) = summary()
    PRINT "Kişi: " + count + " | Ortalama: " + avg + " | En yüksek: " + best

ELSE IF choice = "4" THEN
    DECLARE thresh AS FLOAT = 80.0
    DECLARE names AS LIST[STRING] = list_above(thresh)
    PRINT thresh + "+ olanlar (" + LENGTH(names) + " kişi): " + JOIN(names, ", ") IF names ELSE 'Yok'

ELSE IF choice = "5" THEN
    BREAK
ELSE
    PRINT "Geçersiz seçim."

END WHILE
