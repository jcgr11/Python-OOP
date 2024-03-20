from Course import course
from Student import student
from exceptions import AlreadyEnrolledError, CapacityReachedError, StudentNotFoundError

sie508 = course('SIE508', 3, 5)

bob = student('Bob Sagat', 147258)
sarah = student('Sarah Parker', 258369)
juan = student('Juan Serrano', 789456)
luz = student('Luz Marina', 456123)
akira = student('Akira Toriyama', 3012024)
goku = student('Son Goku', 6191984)
gohan = student('Son Gohan', 10151991)
masashi = student('Masashi Kishimoto', 11111974)
eiichiro = student('Eiichiro Oda', 4051955)
satoshi = student('Satoshi Tajiri', '08281965')

bob.name
sarah.name
juan.name
luz.name
akira.name
goku.name
gohan.name
masashi.name
eiichiro.name
satoshi.name

bob.whoami()
sarah.whoami()
juan.whoami()
luz.whoami()
akira.whoami()
goku.whoami()
gohan.whoami()
masashi.whoami()
eiichiro.whoami()
satoshi.whoami()

students = [bob, sarah, juan, luz, akira, goku, gohan, masashi, eiichiro, satoshi] 
for s in students:
    try:
        sie508.enrollStudent(s)
    except (AlreadyEnrolledError, CapacityReachedError) as e:
        print(e)

sie508.printEnrolled()
sie508.printWaitlisted()

sie508.dropStudent('Bob Sagat')

try:
    sie508.dropStudent('Bob Sagat')
except StudentNotFoundError as e:
    print(e)

sie508.printEnrolled()
sie508.printWaitlisted()
