import express from 'express';

const router = express.Router();

/* GET home page. */
router.get('/', (req, res) => {
  res.render('chat', { title: 'Express' });
});

// Exportar correctamente en ES Modules
export default router;
