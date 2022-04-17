import math
class numerosromanos():
    def __init__(self,numero):
        self.numero=numero

    def descomposion(self):
        decenas=math.trunc(self.numero/10);
        unidades=self.numero%10;

        if self.numero==10:
            print("El numero es X")

        else:

            if(decenas==1):
                decena_romano="l";

            if(decenas==2):
                decena_romano="ll";

            if(decenas==3):
                decena_romano="lll";

            if(decenas==4):
                decena_romano="lV";

            if(decenas==5):
                decena_romano="V";

            if(decenas==6):
                decena_romano="Vl";

            if(decenas==7):
             decena_romano="Vll";

            if(decenas==8):
                decena_romano="Vlll";

            if(decenas==9):
             decena_romano="IX";

###############################
            if(unidades==1):
             unidades_romano="l";

             if(unidades==2):
                 unidades_romano="ll";

            if(unidades==3):
                unidades_romano="lll";

            if(unidades==4):
                unidades_romano="lV";

            if(unidades==5):
                unidades_romano="V";

            if(unidades==6):
                unidades_romano="Vl";

            if(unidades==7):
             unidades_romano="Vll";

             if(unidades==8):
                unidades_romano="Vlll";

            if(unidades==9):
             unidades_romano="IX";


            print("El numero en romano es ",decena_romano+unidades_romano)


romano=numerosromanos(10)
romano.descomposion()