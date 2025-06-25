import { Server } from 'socket.io';
import axios from 'axios';

export function createSocket(server) {
    const io = new Server(server);

    io.on('connection', (socket) => {
        console.log('Cliente conectado');

        socket.on('llama_prompt_rag', async (question) => {
            console.log('Pregunta recibida del cliente:', question);
            
            const url = "http://localhost:8000/llama_prompt_rag";
            const data = { question };
        
            try {
                const response = await axios.post(url, data);        
                const message = response.data.respuesta?.content || "No se recibió respuesta"; 
                              
                socket.emit('respuestaServidor', { message });
                
            } catch (error) {
                console.error("Error en la petición:", error);
                socket.emit('respuestaServidor', { error: "Error al conectar con la API externa" });
            }
        });
        socket.on('llama_finetuning', async (question) => {
            console.log('Pregunta recibida del cliente:', question);
            
            const url = "http://localhost:8000/llama_finetuning";
            const data = { question };
        
            try {
                const response = await axios.post(url, data);        
                const message = response.data.respuesta?.content || "No se recibió respuesta"; 
                              
                socket.emit('respuestaServidor', { message });
                
            } catch (error) {
                console.error("Error en la petición:", error);
                socket.emit('respuestaServidor', { error: "Error al conectar con la API externa" });
            }
        });

        socket.on('llama_prompt', async (question) => {
            console.log('Pregunta recibida del cliente:', question);
            
            const url = "http://localhost:8000/llama_prompt";
            const data = { question };
        
            try {
                const response = await axios.post(url, data);        
                const message = response.data.respuesta?.content || "No se recibió respuesta"; 
                              
                socket.emit('respuestaServidor', { message });
                
            } catch (error) {
                console.error("Error en la petición:", error);
                socket.emit('respuestaServidor', { error: "Error al conectar con la API externa" });
            }
        });                      

        socket.on('disconnect', () => {
            console.log('Cliente desconectado');
        });
    });

    return io;
}
