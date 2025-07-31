import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { WishlistProvider } from "./context/WishlistContext"; 
import Header from "./components/Header";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import HinduWeddingCards from "./components/HinduWeddingCards";
import WishlistPage from "./pages/WishlistPage";
import Description from "./pages/Description"; 
import SimpleCards from "./components/SimpleCards";
import SimpleProductDetail from "./components/SimpleProductDetail";
import Login from "./pages/Login";
import Checkout from "./pages/Checkout";
import OrderConfirmed from "./components/OrderConfirmed";
import WeddingCards from "./pages/WeddingCards";
import AboutUs from "./pages/AboutUs";
import ContactUs from "./pages/ContactUs";
import FAQ from "./pages/FAQ";
import HowToOrder from "./pages/HowToOrder";
import Search from "./pages/Search";
import Cart from "./pages/Cart";
import ScrollToTop from "./components/ScrollToTop";
import "./App.css";

function App() {
  return (
    <WishlistProvider>
      <Router>
        <ScrollToTop />
        <Header />
        <Routes>
          <Route path="/" element={<Home />} />
           <Route path="/login" element={<Login />} />
          <Route path="/Wishlist" element={<WishlistPage />} />
          <Route path="/checkout" element={<Checkout />} />
          <Route path="/order" element={<OrderConfirmed />} />
          <Route path="/hinduWeddingCards" element={<HinduWeddingCards />} />
          <Route path="/product/:id" element={<Description />} />
          <Route path="/" element={<SimpleCards />} /> 
          <Route path="/Simple/:id" element={<SimpleProductDetail />} />
          <Route path="/wedding-cards" element={<WeddingCards />} />
          <Route path="/aboutUs" element={<AboutUs />} />
          <Route path="/contactUs" element={<ContactUs />} />
          <Route path="/FAQ" element={<FAQ />} />
          <Route path="/howToOrder" element={<HowToOrder />} />
          <Route path="/search" element={<Search/>} />
          <Route path="/Cart" element={<Cart/>} />
        </Routes>
        <Footer />
      </Router>
    </WishlistProvider>
  );
}

export default App;

