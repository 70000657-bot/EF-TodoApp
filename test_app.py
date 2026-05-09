import unittest
from app import app, tareas

class TestTodoApp(unittest.TestCase):
    """Pruebas unitarias para la aplicación TodoApp."""

    def setUp(self):
        """Configura el cliente de pruebas antes de cada test."""
        app.config['TESTING'] = True
        self.client = app.test_client()
        tareas.clear()

    def test_pagina_principal_carga(self):
        """Prueba 1: La página principal debe cargar con código 200."""
        respuesta = self.client.get('/')
        self.assertEqual(respuesta.status_code, 200)

    def test_agregar_tarea(self):
        """Prueba 2: Agregar una tarea válida debe guardarla en la lista."""
        self.client.post('/agregar', data={'titulo': 'Tarea de prueba'})
        self.assertEqual(len(tareas), 1)
        self.assertEqual(tareas[0]['titulo'], 'Tarea de prueba')

    def test_tarea_inicia_sin_completar(self):
        """Prueba 3: Una tarea nueva debe iniciar como no completada."""
        self.client.post('/agregar', data={'titulo': 'Nueva tarea'})
        self.assertFalse(tareas[0]['completada'])

    def test_no_agregar_tarea_vacia(self):
        """Prueba 4: No debe agregar tareas con título vacío."""
        self.client.post('/agregar', data={'titulo': ''})
        self.assertEqual(len(tareas), 0)

    def test_completar_tarea(self):
        """Prueba 5: Completar una tarea debe cambiar su estado a True."""
        self.client.post('/agregar', data={'titulo': 'Tarea a completar'})
        tarea_id = tareas[0]['id']
        self.client.get(f'/completar/{tarea_id}')
        self.assertTrue(tareas[0]['completada'])

    def test_eliminar_tarea(self):
        """Prueba 6: Eliminar una tarea debe removerla de la lista."""
        self.client.post('/agregar', data={'titulo': 'Tarea a eliminar'})
        tarea_id = tareas[0]['id']
        self.client.get(f'/eliminar/{tarea_id}')
        self.assertEqual(len(tareas), 0)

if __name__ == '__main__':
    unittest.main()
