import os

archivo = 'tareas.txt'

# --- FUNCIONES DE AYUDA ---
def cargar_tareas():
    """Lee el archivo y devuelve una lista de tareas."""
    if not os.path.exists(archivo): return []
    with open(archivo, 'r', encoding='utf-8') as f:
        return [linea.strip() for linea in f.readlines()]

def guardar_tareas(tareas):
    """Sobrescribe el archivo con la lista actual de tareas."""
    with open(archivo, 'w', encoding='utf-8') as f:
        for tarea in tareas:
            f.write(tarea + '\n')

# --- BUCLE PRINCIPAL (EVENT LOOP) ---
while True:
    # Limpia la consola en Linux para dar el efecto de "refrescar pantalla"
    os.system('clear') 
    
    tareas = cargar_tareas()

    # 1. PANTALLA DE VISUALIZACIÓN
    print("=== TU LISTA DE TAREAS ===")
    if not tareas:
        print("(La lista está vacía)\n")
    else:
        for i, t in enumerate(tareas):
            print(f"[{i + 1}] {t}")
        print() # Salto de línea extra
    
    # 2. LOS "BOTONES" DEL MENÚ
    print("--- QUÉ DESEAS HACER ---")
    print("[1] ➕ Agregar tarea")
    print("[2] ❌ Eliminar tarea")
    print("[3] 🗑️  Limpiar todo")
    print("[0] 🚪 Salir")
    
    # 3. CAPTURA DE LA ACCIÓN
    opcion = input("\nSelecciona el número de la opción: ")

    # 4. ENRUTAMIENTO DE LA LÓGICA
    if opcion == '1':
        nueva = input("Escribe la nueva tarea: ")
        if nueva.strip(): # Evita guardar tareas vacías
            tareas.append(nueva)
            guardar_tareas(tareas)
            
    elif opcion == '2':
        if tareas:
            idx = input("Escribe el número de la tarea a eliminar: ")
            if idx.isdigit() and 1 <= int(idx) <= len(tareas):
                # pop() extrae y elimina el elemento de la lista en memoria
                tareas.pop(int(idx) - 1) 
                guardar_tareas(tareas)
            else:
                input("Número no válido. Presiona Enter para intentar de nuevo...")
                
    elif opcion == '3':
        seguro = input("¿Seguro que quieres borrar TODO? (s/n): ")
        if seguro.lower() == 's':
            guardar_tareas([]) # Guardar una lista vacía limpia el archivo
            
    elif opcion == '0':
        os.system('clear')
        print("¡Programa terminado. Hasta luego!")
        break # Rompe el bucle while y finaliza el programa
        
    else:
        input("Opción no reconocida. Presiona Enter para continuar...")