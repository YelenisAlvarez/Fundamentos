import modelo 
import controlador 
import vista 

def main():
  opcion = 0 

  while opcion != 7:
    opcion = vista.mostrar_menu()
    controlador.ejecutar_opcion(opcion)

    if opcion !=7
       input("\nPresione Enter para continuar...")

if __name__== "__main__":
  main() 
