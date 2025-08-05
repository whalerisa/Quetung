const express = require('express')
const cors = require('cors')
const app = express()

app.use(cors())
app.use(express.json())

app.post('/api/data', (req, res) => {
  console.log(req.body)
  res.json({ message: 'Data received' })
})

app.listen(3000, () => console.log('Backend running on http://localhost:3000'))
