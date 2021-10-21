function [XR,EA,M] = NewtonRhapson2Fcn(f,df,xi,Niter,es)
 
% ESTA FUNCION PIDE LOS SIGUIENTES DATOS DE ENTRADA:
 
% f = función anónima dependiente de una variable ej. @(x) cos(x) + x
% df = derivada de la función anónima ej. @(x) 1 - sin(x) MANUALMENTE DEBES
% SABER SI LA DERIVADA ES CORRECTA
% xi = Valor inicial de x. Este dato es un escalar.
% Niter = Número de iteraciones.
% es = Error relativo porcentual máximo. 
 
% VARIABLES DE SALIDA:
 
% XR = Ultima iteración de la raíz de la función.
% ER = Ultima iteracion del error relativo.
% M = Tabla de resultados {'xi','Error relativo (%)'}
 
%METODOS DE SOLUCION
 
%Método 1: Si Niter está vacío (Niter = []) entonces se debe especificar un
%error relativo máximo para converger.
%Método 2: Si Tol está vacío (Tol = []) entonces se debe especificar un
%número máximo de iteraciones para el código. Es posible que un número muy
%grande de iteraciones cree un error y un mensaje aparecerá sugiriendo
%reducir el número de iteraciones.
 
%Protección contra errores en las entradas.
if nargin ~= 5                 
    error('Se necesita definir una función, un valor inicial, un número máximo de iteraciones y un error aproximado máximo');
%Si se ingresan todos los datos de entrada, elegir un método de solución
else                          
    if  isempty(Niter) == 1 
        metodo = 1; Niter = 1000; disp(newline);
        disp('Solución por error aproximado máximo para converger');
    elseif isempty(es) == 1 
        metodo = 2; disp(newline);
        disp('Solución por número máximo de iteraciones para converger');
    elseif isempty(Niter) == 0 && isempty(es) == 0
        error('"Niter" y "es" no pueden tener un dato de entrada al mismo tiempo, uno de los dos debe estar vacío (ejemplo: Niter = [])');
    end
end
 
if df(xi) == 0
    error('Derivada de la función igual a cero en este punto de x. Utilice otro valor inicial para x');
end
 
for i = 1:Niter + 1
    xi_2(i) = xi(i) - f(xi(i))/df(xi(i));
    xi(i+1) = xi_2(i); fxi(i) = f(xi(i));
    ea(i) = abs((xi_2(i) - xi(i)) / xi_2(i)) * 100; %Calcula el error relativo actual
    
    if i >= 2
        if xi(i+1) == xi(i-1) && ea(i) > es
            osc = osc + 1;
            if osc == 3
                error('Divergencia oscilatoria detectada. Use otro valor inicial de x');
            end
        end
    end
    
    if i >= 30 && ea(i) > es
        error('Convergencia lenta o divergencia detectada. Use otro valor inicial de x');
    end
        
    if metodo == 1
        if ea(i) < es %Si el error relativo es menor a la tolerancia exigida, se acaba el ciclo.
            break;
        end
    end
end
 
M1 = {'xi', 'f(xi)','Error relativo (%)'};
M2 = num2cell([xi(1:end-1)',fxi',ea']);
M = [M1; M2]; XR = xi(end); EA = ea(end);

CORRIDA PROGRAMA

>> [XR,EA,M] = NewtonRhapson2Fcn(@(x) sqrt(x^3-sin(x))-log(cos(x))-3, @(x) ((3*x^2 -cos(x))/(2*sqrt(x^3 -sin(x))))+(sin(x)/cos(x)),1,[],0.0001)


Solución por error aproximado máximo para converger

XR =

   1.387307605629658


EA =

     1.086357317296665e-07


M =

  6×3 cell array

    {'xi'               }    {'f(xi)'                }    {'Error relativo (%)'   }
    {[                1]}    {[   -1.986216506327816]}    {[   29.946823608062466]}
    {[1.427487019867797]}    {[    0.331479899805526]}    {[    2.623051821600543]}
    {[1.391000359596920]}    {[    0.028055428775768]}    {[    0.264193782637598]}
    {[1.387335106501195]}    {[2.074005583851957e-04]}    {[    0.001982211031186]}
    {[1.387307607136770]}    {[1.136541039059580e-08]}    {[1.086357317296665e-07]}