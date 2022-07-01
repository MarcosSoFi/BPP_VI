
# Cementos
class cemento_cem1: 
    """"
    Según la Instrucción para la recepción de cementos (RC-16)
    Cementos Comunes - CEM I - Cemento Portland

    >>> cem_1   = cemento_cem1("CEM I","42,5","N","Cemento Portland","Granel",131.82,"2020-06-22","1")
    >>> d_cem_1 = cem_1.dname_cem1()
    >>> print(d_cem_1)
    >>> CEM I 42,5 N

    """
    def __init__(self,tc,rc,ric,dn,metodo,precio,fecha,dosificacion):
        """
        Constructor de la clase CEM I

        :param tc:      tipo de cemento             CEM I
        :type  tc:      :class:`string`       
        :param rc:      resistencia cemento         32,5/42,5/52,5
        :type  rc:      :class:`string`
        :param ric:     resistencia inicia          R/N
        :type  ric:     :class:`string`
        :param dn:      designación                 Cemento Portland
        :type  dn:      :class:`string`
        :param metodo:  metodo de distribucion      Granel/Sacos
        :type  metodo:  :class:`string`

        :param precio:  precio  
        :type  precio:  :class:`float`
        :param fecha:   fecha  
        :type  fecha:   :class:`string``
        :param dosificacion:   fecha  
        :type  dosificacion:  :class:`string``

        """
        self.tc=tc
        self.rc=rc
        self.ric=ric
        self.dn=dn
        self.metodo=metodo
        self.precio=precio
        self.fecha=fecha
        self.dosificacion=dosificacion

    def dname_cem1(self):
        """
        Metodo para crear la designacion de los cementos CEM I - CEM I 42,5 N
        """
        dname_c1 = f'{self.tc} {self.rc} {self.ric}'
        return dname_c1   

class cemento_cem2(cemento_cem1):
    """ 
        Según la Instrucción para la recepción de cementos (RC-16)
        Cementos comunes - CEM II - Cemento Portland con adiciones

        >>> cem_2   = cemento_cem2("CEM II","A","L","32,5","R","Cemento Portland con Caliza","Granel",106.96,"2020-06-22","1")
        >>> d_cem_2 = cem_2.dname_cem2()
        >>> print(d_cem_2)
        >>> CEM II/A-L 32,5 R

    """
    def __init__(self,tc,st,ca,rc,ric,dn,metodo,precio,fecha,dosificacion):
        cemento_cem1.__init__(self,tc,rc,ric,dn,metodo,precio,fecha,dosificacion)
        """
        Constructor de la clase CEM II

        :param tc:      tipo de cemento             CEM II
        :type  tc:      :class:`string`
        :param st:      subtipo                     A/B
        :type  st:      :class:`string`
        :param ca:      caracterista adicional      S/D/M/P/Q/V/W/T/L/LL
        :type  ca:      :class:`string`
        :param rc:      resistencia cemento         32,5/42,5/52,5
        :type  rc:      :class:`string`
        :param ric:     resistencia inicia          R/N
        :type  ric:     :class:`string`
        :param dn:      designación                 Cemento Portland
        :type  dn:      :class:`string`
        :param metodo:  metodo de distribucion      Granel/Sacos
        :type  metodo:  :class:`string`

        :param precio:  precio  
        :type  precio:  :class:`float`
        :param fecha:   fecha  
        :type  fecha:   :class:`string``
        :param dosificacion:   fecha  
        :type  dosificacion:  :class:`string``

        """
        self.st=st
        self.ca=ca 

    def dname_cem2(self):
        """
        Metodo para crear la designacion de los cementos CEM II - CEM II/A-L 32,5 R
        
        """
        dname_c2=f'{self.tc}/{self.st}-{self.ca} {self.rc} {self.ric}'
        return dname_c2
    



#cem_1   = cemento_cem1("CEM I","42,5","N","Cemento Portland","Granel",131.82,"2020-06-22","1")
#d_cem_1 = cem_1.dname_cem1()
#print(d_cem_1)


#cem_2   = cemento_cem2("CEM II","A","L","32,5","R","Cemento Portland con Caliza","Granel",106.96,"2020-06-22","1")
#d_cem_2 = cem_2.dname_cem2()
#print(d_cem_2)