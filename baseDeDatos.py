def registrarCliente():
    print("\n" + "="*30)
    print(" REGISTRO DE NUEVO CLIENTE ".center(30, "="))
    nif = input("\n🔢 NIF del cliente: ").strip()
    
    if nif in baseClientes:
        print("\n⚠️  Error: Este NIF ya está registrado")
        return
    
    print("\n📝 Ingrese los datos del cliente:")
    datosCliente = {
        'nombre': input("👤 Nombre completo: ").title(),
        'direccion': input("🏠 Dirección: "),
        'telefono': input("📱 Teléfono: "),
        'correo': input("✉️  Correo electrónico: ").lower(),
        'preferente': input("\n⭐ ¿Cliente preferente? (s/n): ").lower() == 's'
    }
    
    baseClientes[nif] = datosCliente
    print("\n✅ Cliente registrado exitosamente!")

def eliminarCliente():
    print("\n" + "="*30)
    print(" ELIMINAR CLIENTE ".center(30, "="))
    nif = input("\n🔢 NIF del cliente a eliminar: ").strip()
    
    if nif in baseClientes:
        del baseClientes[nif]
        print("\n🗑️  Cliente eliminado correctamente")
    else:
        print("\n⚠️  Error: NIF no encontrado")

def mostrarCliente():
    print("\n" + "="*30)
    print(" DATOS DEL CLIENTE ".center(30, "="))
    nif = input("\n🔢 NIF del cliente a consultar: ").strip()
    
    if nif in baseClientes:
        print("\n📋 Información del cliente:")
        for clave, valor in baseClientes[nif].items():
            print(f"• {clave.capitalize()}: {valor}")
    else:
        print("\n⚠️  Error: Cliente no registrado")

def listarClientes():
    print("\n" + "="*30)
    print(" LISTADO COMPLETO ".center(30, "="))
    
    if not baseClientes:
        print("\n📭 No hay clientes registrados")
        return
    
    print(f"\n👥 Total de clientes: {len(baseClientes)}")
    for nif, datos in baseClientes.items():
        print(f"\n🔹 NIF: {nif}")
        print(f"👤 Nombre: {datos['nombre']}")
        print(f"📞 Teléfono: {datos['telefono']}")

def listarPreferentes():
    print("\n" + "="*30)
    print(" CLIENTES PREFERENTES ".center(30, "="))
    preferentes = {nif: datos for nif, datos in baseClientes.items() if datos['preferente']}
    
    if not preferentes:
        print("\n⭐ No hay clientes preferentes")
        return
    
    print(f"\n🌟 Total preferentes: {len(preferentes)}")
    for nif, datos in preferentes.items():
        print(f"\n🔸 NIF: {nif}")
        print(f"👤 Nombre: {datos['nombre']}")
        print(f"✉️  Email: {datos['correo']}")

def mostrarMenu():
    print("\n" + "="*30)
    print(" GESTIÓN DE CLIENTES ".center(30, "="))
    print("\n1. Registrar cliente")
    print("2. Eliminar cliente")
    print("3. Consultar cliente")
    print("4. Listar todos")
    print("5. Listar preferentes")
    print("6. Salir")

baseClientes = {}  


opcion = ""
while opcion != "6":
    mostrarMenu()
    opcion = input("\n➡️  Seleccione una opción (1-6): ").strip()
    
    match opcion:
        case "1":
            registrarCliente()
        case "2":
            eliminarCliente()
        case "3":
            mostrarCliente()
        case "4":
            listarClientes()
        case "5":
            listarPreferentes()
        case "6":
            print("\n👋 Programa terminado")
        case _:
            print("\n⚠️  Opción no válida")