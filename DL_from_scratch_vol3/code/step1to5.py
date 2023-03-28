import numpy as np


class Variable:
    def __init__(self, data):
        self.data = data


class Function:
    """모든 함수에 공통되는 기능을 구현한 기반 클래스
    구체적인 함수는 Function 클래스를 상속한 클래스에서 구현 
    """    
    def __call__(self, input): 
        """
        input의 data값으로 forward 메서드에서 정의된 연산을 수행
        Args:
            input (_class_Variable): Variable의 instance 

        Returns:
            _class_Variable: forward 메서드 수행결과 
        """        
        x = input.data
        y = self.forward(x) 
        output = Variable(y)
        self.input = input
        self.output = output
        return output

    def forward(self, x):
        raise NotImplementedError() #forward 메서드는 반드시 상속하여 구현해야 함 
    
class Square(Function):
    """Function 클래스를 상속하여 입력값을 제곱하는 클래스 
    forward 메서드에서 수행할 연산을 정의
    Args:
        Function (_class_Function)
    """    
    def forward(self, x):
        return x ** 2


class Exp(Function):
    """Function 클래스를 상속하여 e^x 값을 구함 

    Args:
        Function (_class_Function)
    """    
    def forward(self, x):
        return np.exp(x)


def numerical_diff(f, x, eps=1e-4):
    """중앙차분(centerted difference)을 이용하여 수치 미분을 계산 

    Args:
        f (_class_Function): 미분 대상이 되는 함수
        x (_class_Variable): 미분을 계산하는 변수 
        eps (float, optional): epsilon(작은 값) Defaults to 1e-4.

    Returns:
        float: 수치 미분값 
    """    
    x0 = Variable(x.data - eps)
    x1 = Variable(x.data + eps)
    y0 = f(x0)
    y1 = f(x1)
    return (y1.data - y0.data) / (2 * eps)

def f(x):
    """y = e(x^2)^2 값을 구함 

    Args:
        x (_class_Variable)

    Returns:
        _class_Variable: e(x^2)^2 값
    """    
    A = Square()
    B = Exp()
    C = Square()
    return C(B(A(x)))

g = Square()
x1 = Variable(np.array(2.0))
dy1 = numerical_diff(g, x1)
print("type of g", type(g))
print("type of x1", type(x1))
print("numerical diff of square function g {:.2f}".format(dy1))

x2 = Variable(np.array(0.5))
dy2 = numerical_diff(f, x2)
print("type of f", type(f))
print("type of x2", type(x2))
print("numerical diff of square function f {:.2f}".format(dy2))


'''Result
type of g <class '__main__.Square'>
type of x1 <class '__main__.Variable'>
numerical diff of square function g 4.00
type of f <class 'function'>
type of x2 <class '__main__.Variable'>
numerical diff of square function f 3.30
'''
