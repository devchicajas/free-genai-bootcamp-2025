
# **Plataforma de Aprendizaje de Japonés con IA**  

## **Descripción General**  
Este proyecto está enfocado en construir un **sistema de aprendizaje de japonés impulsado por IA**, diseñado para ejecutarse en **infraestructura propia** con el fin de **reducir costos en la nube y mantener la privacidad y seguridad**. Comenzamos con **japonés**, pero el objetivo a largo plazo es **expandirse al chino**.  

El sistema proporciona varias **actividades de estudio**, utilizando **LLMs de código abierto** y **Generación Aumentada por Recuperación (RAG)** para ayudar a los estudiantes a mejorar su vocabulario, construcción de oraciones e inmersión en el idioma.  

---

## **Requisitos Funcionales**  
- **IA autoalojada**: El sistema se ejecutará en **nuestro propio hardware** (PC de IA con un presupuesto de ~$10K–$15K) en lugar de depender de la nube, para **mantener los costos bajos y la privacidad de los datos**.  
- **Modelo LLM de 80B parámetros**: Se utilizará un **LLM de código abierto con 80B parámetros** para garantizar **escalabilidad a largo plazo**, especialmente cuando expandamos al **idioma chino**.  
- **Actividades de Estudio**: Los estudiantes interactuarán con un **Portal de Aprendizaje** que incluirá:  
  - Práctica de escritura  
  - Inmersión en aventura de texto  
  - Lectura de novelas visuales ligeras  
  - Constructor de oraciones (impulsado por IA)  
  - Tarjetas de vocabulario visuales  
  - Aprendizaje mediante conversación  
- **Generación Aumentada por Recuperación (RAG)**: La función de **Constructor de Oraciones** utilizará un **banco de vocabulario estructurado** para asegurar la **formación de oraciones precisas y naturales**.  
- **Guardrails y Seguridad**: Se implementarán filtros de **entrada y salida** para evitar **contenido inadecuado** y garantizar un **entorno de aprendizaje seguro**.  

---

## **Suposiciones**  
- El **LLM de 80B parámetros** debería ser **lo suficientemente eficiente** para nuestro caso de uso, mientras **garantizamos escalabilidad** en el futuro.  
- Un **único servidor con IA** será suficiente para soportar **300 estudiantes activos** en **Nagasaki**, con una **conexión a internet estable** para interacciones en línea.  
- Se utilizarán **modelos de código abierto siempre que sea posible**, pero también se aplicarán **capas de seguridad** para evitar cualquier **exposición de datos de los estudiantes**.  
- **El rango de edad de los estudiantes es variado**, por lo que se necesitarán **filtros de contenido y respuestas contextuales de la IA** para **mantener interacciones apropiadas**.  
- Se priorizará la **eficiencia del hardware**—ya que evitamos soluciones en la nube por **restricciones presupuestarias**, el sistema debe estar **optimizado para el procesamiento local**.  

---

## **Estrategia de Datos**  
- **No utilizaremos datos externos no verificados**—compraremos y curaremos materiales de aprendizaje para **evitar problemas de derechos de autor** y los almacenaremos en una **base de datos segura**.  
- **El historial de estudio de los estudiantes no será almacenado**, y el modelo **no se entrenará con datos generados por usuarios** para evitar preocupaciones sobre **privacidad**.  
- La **base de datos con 2000 palabras esenciales** servirá como referencia para garantizar que la IA genere **respuestas lingüísticas precisas y útiles**.  
- La base de datos se actualizará regularmente para incluir **nuevas palabras, estructuras de oraciones y reglas gramaticales**, asegurando contenido preciso y actualizado.  
- Se implementará **filtrado de prompts y moderación de respuestas** para garantizar que la **IA genere contenido educativo relevante**.  

---

## **Consideraciones**  
- **IBM Granite** es un modelo prometedor, ya que es **totalmente de código abierto** y su **origen de datos es rastreable**, lo que minimiza los riesgos de **problemas de derechos de autor**.  
- Dado que el sistema será **autoalojado**, es importante **optimizar el rendimiento computacional** para que el servidor pueda manejar el procesamiento de la IA **dentro de las limitaciones de hardware**.  
- **El ancho de banda y la latencia** deben ser monitoreados a medida que **aumenta la cantidad de estudiantes**, garantizando **respuestas en tiempo real** sin interrupciones.  
- Si la cantidad de estudiantes crece, será necesario **evaluar la escalabilidad del sistema**, considerando **ampliar el hardware o adoptar soluciones híbridas**.  
- **El cumplimiento de regulaciones de privacidad** (similares a GDPR en Japón) es fundamental, especialmente en el manejo de **contenido generado por los usuarios**.  

---

## **Stack Tecnológico**  
- **Modelo LLM**: IBM Granite (código abierto)  
- **Backend**: Generación Aumentada por Recuperación (RAG)  
- **Base de Datos**: Banco de palabras (2000 palabras esenciales)  
- **Seguridad**: Guardrails de entrada y salida para moderación de contenido  
- **Hardware**: PC con IA con un presupuesto de $10K–$15K  

---

## **Planes Futuros**  
- **Escalar para soportar el aprendizaje de chino**  
- **Expandir la base de datos de vocabulario más allá de las 2000 palabras esenciales**  
- **Mejorar la calidad de las respuestas de IA mediante ingeniería de prompts**  
- **Explorar modelos de IA adicionales de código abierto** para mejorar el rendimiento  

---

### **Licencia**  
Este proyecto sigue un **modelo de código abierto**, pero **todos los materiales educativos y conjuntos de datos utilizados están licenciados** según corresponda.  

---

