+----------------------+
|        Banco         |
+----------------------+
| - nombre: str        |
| - codigo_banco: str  |
| - direccion: str     |
+----------------------+
| + transferir(cuenta_origen: Cuenta, cuenta_destino: Cuenta, monto: float) |
+----------------------+

+--------------------+
|      Cliente       |
+--------------------+
| - nombre: str      |
| - direccion: str   |
| - num_identificacion: str |
+--------------------+
| + obtener_datos(): str |
+--------------------+

           ▲
           |
+-----------------------+
|        Cuenta         |
+-----------------------+
| - num_cuenta: str     |
| - titular: Cliente    |
| - saldo: float        |
+-----------------------+
| + depositar(monto: float)           |
| + retirar(monto: float): bool       |
| + consultar_saldo(): float          |
+-----------------------+

           ▲
      ______|_______
      |             |
+-----------------------+      +-----------------------+
|  CuentaAhorros       |      |    CuentaCorriente    |
+-----------------------+      +-----------------------+
| - cantidad_retiros: int     | - limite: float       |
+-----------------------+      +-----------------------+
| + retirar(monto: float): bool | + retirar(monto: float): bool |
+-----------------------+      +-----------------------+

Explicación del Diagrama:

	•	Clase Banco:
	•	Atributos: nombre, codigo_banco, direccion.
	•	Método: transferir(cuenta_origen, cuenta_destino, monto), que permite transferir dinero entre cuentas.
	•	Clase Cliente:
	•	Atributos: nombre, direccion, num_identificacion.
	•	Método: obtener_datos(), que devuelve la información del cliente.
	•	Clase Cuenta (abstracta):
	•	Atributos: num_cuenta, titular (instancia de Cliente), saldo.
	•	Métodos:
	•	depositar(monto): para depositar dinero.
	•	retirar(monto): método a sobrescribir en cada tipo de cuenta.
	•	consultar_saldo(): retorna el saldo actual de la cuenta.
	•	Clase CuentaAhorros (hereda de Cuenta):
	•	Atributo: cantidad_retiros, que cuenta la cantidad de retiros realizados.
	•	Método:
	•	retirar(monto): permite realizar retiros y actualiza cantidad_retiros. No permite saldo negativo.
	•	Clase CuentaCorriente (hereda de Cuenta):
	•	Atributo: limite, que define el límite de sobregiro permitido.
	•	Método:
	•	retirar(monto): permite retiros hasta el límite, con saldo negativo (“en rojo”) si excede el saldo disponible.