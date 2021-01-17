import './App.css';
import MyNavbar from "../src/components/my-navbar/my-navbar.component";
import { BrowserRouter as Router, Route, Switch} from "react-router-dom";
import Home from "../src/pages/Home";
import Interview  from "../src/pages/Interview";
import Results from "../src/pages/Results";


function App() {
  return (
    
    <Router>
      <div className="App">
      <MyNavbar/>
     
      <Switch> 
        <Route path="/Home" exact component={Home} /> 
        <Route path="/Interview" exact component={Interview} /> 
        <Route path="/Results" exact component={Results} /> 
      </Switch>
      
    </div>
    </Router>
  );
}

export default App;
