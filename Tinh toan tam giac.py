import math

class diem:
    '''xac dinh tinh chat toa do mot diem'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def khoangcach(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
    
class vector:
    '''xac dinh cac tinh chat cua vector'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    #nhan vactor voi mot so
    def __mul__(self, a):
        return vector(self.x*a, self.y*a)
                    
    def dodaivector(self):
        return math.sqrt(self.x**2 + self.y **2)

    def nhanvohuong(self, other):
        return self.x*other.x + self.y*other.y

    def goc(self, other):
        tu = self.nhanvohuong(other)
        mau = (self.dodaivector()*other.dodaivector())
        return math.acos(tu/mau)
    
def kiemtra_dauvao(n): #check dau vao dung format
    try:
        if type(n) is list and len(n) == 6:
            for i in n:
                if type(i) is int or type(i) is float:
                    continue
                else:
                    print('Dau vao chua dung format')
                    quit()
            return True
        else:
            print('Dau vao chua dung format')
            quit()
    except:
        print('Dau vao chua dung format')
        quit()

def chuyendoi_dauvao(n):
    kiemtra_dauvao(n)    
    A = diem(n[0], n[1])
    B = diem(n[2], n[3])
    C = diem(n[4], n[5])
    vectorAB = vector(B.getX() - A.getX(), B.getY() - A.getY())
    vectorBC = vector(C.getX() - B.getX(), C.getY() - B.getY())
    vectorAC = vector(C.getX() - A.getX(), C.getY() - A.getY())
    return A, B, C, vectorAB, vectorBC, vectorAC
   
def kiemtra_tamgiac(n):
    kiemtra_dauvao(n)  
    A, B, C, vectorAB, vectorBC, vectorAC = chuyendoi_dauvao(n)
    AB = vectorAB.dodaivector()
    AC = vectorAC.dodaivector()
    BC = vectorBC.dodaivector()
    if AB < AC + BC and AC < BC + AB and BC < AB + AC:
            return True
    return False
    
def goccanh_tamgiac(n):
    if kiemtra_tamgiac(n):
        A, B, C, vectorAB, vectorBC, vectorAC = chuyendoi_dauvao(n)
        AB = round(vectorAB.dodaivector(), 2)
        AC = round(vectorAC.dodaivector(), 2)
        BC = round(vectorBC.dodaivector(), 2)
        gocA = round(vectorAB.goc(vectorAC)*180/math.pi, 2)
        gocB = round(vectorBC.goc(vectorAB*-1)*180/math.pi, 2)
        gocC = round(vectorAC.goc(vectorBC)*180/math.pi, 2)
        return [AB, BC, AC, gocA, gocB, gocC]
    return 'A, B, C khong hop thanh mot tam giac'
        
def xet_tamgiac(n):
    if kiemtra_tamgiac(n):
        A, B, C, vectorAB, vectorBC, vectorAC = chuyendoi_dauvao(n)
        AB = vectorAB.dodaivector()
        AC = vectorAC.dodaivector()
        BC = vectorBC.dodaivector()
        gocA = vectorAB.goc(vectorAC)
        gocB = vectorBC.goc(vectorAB*-1)
        gocC = vectorAC.goc(vectorBC)
        #gocdoi = {'AB': 'C', 'BC': 'A', 'AC': 'B'}  
        if math.isclose(AB, AC, rel_tol = 1e-04) and math.isclose(AB, BC, rel_tol = 1e-04):
            return 'ABC la tam giac deu'
        elif math.isclose(AB, AC, rel_tol = 1e-04):
            if vectorAB.nhanvohuong(vectorAC) == 0:
                return 'ABC la tam giac vuong can tai dinh A'
            elif gocA > math.pi/2:
                return 'ABC la tam giac tu va can tai dinh A'
            else:
                return 'ABC la tam giac can tai dinh A'
        elif math.isclose(AC, BC, rel_tol = 1e-04):
            if vectorAC.nhanvohuong(vectorBC) == 0:
                return 'ABC la tam giac vuong can tai dinh C'
            elif gocC > math.pi/2:
                return 'ABC la tam giac tu va can tai dinh C'
            else:
                return 'ABC la tam giac can tai dinh C'
        elif math.isclose(AB, BC, rel_tol = 1e-04):
            if vectorAB.nhanvohuong(vectorBC) == 0:
                return 'ABC la tam giac vuong can tai dinh B'
            elif gocB > math.pi/2:
                return 'ABC la tam giac tu va can tai dinh B'
            else:
                return 'ABC la tam giac can tai dinh B'
        elif vectorAB.nhanvohuong(vectorBC) == 0:
            return 'ABC la tam giac vuong tai dinh B va la tam giac vuong'
        elif vectorAB.nhanvohuong(vectorAC) == 0:
            return 'ABC la tam giac vuong tai dinh A va la tam giac vuong'
        elif vectorBC.nhanvohuong(vectorAC) == 0:
            return 'ABC la tam giac vuong tai dinh C va la tam giac vuong'
        elif gocA > math.pi/2:
            return 'ABC la tam giac tu tai dinh A va la tam giac thuong'
        elif gocB > math.pi/2:
            return 'ABC la tam giac tu tai dinh B va la tam giac thuong'
        elif gocC > math.pi/2:
            return 'ABC la tam giac tu tai dinh C va la tam giac thuong'
        else:
            return 'ABC la tam giac nhon tai dinh A va la tam giac thuong'
    return 'A, B, C khong hop thanh mot tam giac'


def dientich_tamgiac(n):
    if kiemtra_tamgiac(n):
        A, B, C, vectorAB, vectorBC, vectorAC = chuyendoi_dauvao(n)
        return round(0.5*abs((B.getX() - A.getX())*(C.getY() -A.getY()) - (C.getX() - A.getX())*(B.getY() -A.getY())), 2)
    return 'A, B, C khong hop thanh mot tam giac'

def duongcao_tamgiac(n):
    if kiemtra_tamgiac(n):
        A, B, C, vectorAB, vectorBC, vectorAC = chuyendoi_dauvao(n)
        dcA = round(2*dientich_tamgiac(n)/vectorBC.dodaivector(), 2)
        dcB = round(2*dientich_tamgiac(n)/vectorAC.dodaivector(), 2)
        dcC = round(2*dientich_tamgiac(n)/vectorAB.dodaivector(), 2)
        return [dcA, dcB, dcC]
    return 'A, B, C khong hop thanh mot tam giac'

def trongtam(n):
    if kiemtra_tamgiac(n):
        A, B, C, vectorAB, vectorBC, vectorAC = chuyendoi_dauvao(n)
        xtrongtam = (A.getX() + B.getX() + C.getX())/3
        ytrongtam = (A.getY() + B.getY() + C.getY())/3
        trongtam = diem(xtrongtam, ytrongtam)
        return trongtam
    
def trungtuyen_tamgiac(n):
    if kiemtra_tamgiac(n):
        A, B, C, vectorAB, vectorBC, vectorAC = chuyendoi_dauvao(n)
        ttA = round(A.khoangcach(trongtam(n)), 2)
        ttB = round(B.khoangcach(trongtam(n)), 2)
        ttC = round(C.khoangcach(trongtam(n)), 2)
        return [ttA, ttB, ttC]
    return 'A, B, C khong hop thanh mot tam giac'

def giaima_tamgiac(n):
    if kiemtra_tamgiac(n):
        print('A, B, C hop thanh mot tam giac')
        
        gctg = goccanh_tamgiac(n)
        print('1. So do co ban cua tam giac:')
        print('Chieu dai canh AB:', gctg[0])
        print('Chieu dai canh BC:', gctg[1])
        print('Chieu dai canh CA:', gctg[2])
        print('Goc A:', gctg[3])
        print('Goc B:', gctg[4])
        print('Goc C:', gctg[5])       
        print(xet_tamgiac(n))
        print('2. Dien tich cua tam giac ABC:', dientich_tamgiac(n))
        
        dctg = duongcao_tamgiac(n)
        print('3. So do nang cao tam giac ABC:')
        print('Do dai duong cao tu dinh A:', dctg[0])
        print('Do dai duong cao tu dinh B:', dctg[1])
        print('Do dai duong cao tu dinh C:', dctg[2])
        
        tttg = trungtuyen_tamgiac(n)
        print('Khoang cach den trong tam tu dinh A:', tttg[0])
        print('Khoang cach den trong tam tu dinh B:', tttg[1])
        print('Khoang cach den trong tam tu dinh C:', tttg[2])

        tt = trongtam(n)
        print('4. Toa do mot so diem dac biet cua tam giac ABC:')
        print('Toa do trong tam: [{}, {}]'.format(round(tt.getX(), 2), round(tt.getY(), 2)))
        
    else:
        print('A, B, C khong hop thanh mot tam giac')
        quit()
n = list()
toa_do = ['Ax', 'Ay', 'Bx', 'By', 'Cx', 'Cy']
for u, v in enumerate(toa_do):
    while True:
        try: 
            n.append(int(input(f'Nhap toa do {v}: ')))
            break
        except:
            print('Vui long nhap mot so')
            continue









        
    

