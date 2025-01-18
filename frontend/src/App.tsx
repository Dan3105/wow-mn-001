import './App.css'
import AppRouter from './lib/router'
import { ToastProvider } from './shared_components/toaster'

function App() {

  return (
    <>
      <div>
        <ToastProvider/>
        <AppRouter />
      </div>
    </>
  )
}

export default App
