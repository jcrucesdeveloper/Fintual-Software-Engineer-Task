# Tarea para postular al puesto de Software Engineer en Fintual

> "Construct a simple Portfolio class that has a collection of Stocks. Assume each Stock has a "Current Price" method that receives the last available price. Also, the Portfolio class has a collection of "allocated" Stocks that represents the distribution of the Stocks the Portfolio is aiming (i.e. 40% META, 60% APPL)
>
> Provide a portfolio rebalance method to know which Stocks should be sold and which ones should be bought to have a balanced Portfolio based on the portfolio's allocation.
>
> Add documentation/comments to understand your thinking process and solution"

## Consideraciones tomadas

- Código y comentarios en inglés
- Comentarios usando docstring de una linea
- Tres acciones para balancear el portafolio: Comprar, Vender y Mantener
- Acciones escritas como variables globales constantes CON MAYUSCULAS (ójala python tuviera enums antes de la 3.4)
- 2 decimales de output
- Dos casos de prueba en dos portafolios distintos
- Se agregaron métodos auxiliares para ordenar el output

## Para rebalancear el portafolio:

1. **Calcular valor actual del portafolio**: Suma el valor de los stocks(shares × precio actual)
2. **Determinar asignación objetivo**: Para cada stock, calcular el valor objetivo basado en su porcentaje de asignación
3. **Calcular shares objetivo**: Dividir valor objetivo por precio actual para obtener el número de shares objetivo
4. **Computar acciones de rebalanceo**: Comparar shares objetivo con shares actuales:
   - **Comprar** si objetivo > actual (diferencia positiva, necesito más shares)
   - **Vender** si objetivo < actual (diferencia negativa, hay que vender)
   - **Mantener** si objetivo = actual (sin diferencia, nada)

## Chat LLM

Para preguntar algunos conceptos y una sintaxis de list comprehension de python:
[ChatGPT Conversation](https://chatgpt.com/share/68f17129-125c-800b-8a55-7c81ceeca19c)
