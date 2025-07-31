// HinduWeddingCards.jsx
import React, { useState } from 'react';
import { FaHeart } from 'react-icons/fa';
import { useNavigate } from 'react-router-dom';

// Image imports
import BlueLove from '../assets/images/beach-card.png';
import Ganasha from '../assets/images/ganesha.png';
import FavourBox from '../assets/images/favour-box.png';
import Theme from '../assets/images/theme.png';
import Vintage from '../assets/images/vintage.png';
import Peacock from '../assets/images/peacock.png';
import Unique from '../assets/images/unique.jpg';
import Wardrobe from '../assets/images/wardrobe.png';
import Foldable from '../assets/images/foldable.jpg';
import Traditional from '../assets/images/traditional2.png';
import Scroll from '../assets/images/scroll.png';
import Gatefold from '../assets/images/gatefold.png';

const cards = [
  { id: 1, title: "Blue Love Wedding Cards", price: "Rs. 72.25", image: BlueLove },
  { id: 2, title: "Ganesha Wedding Cards", price: "Rs. 52.25", image: Ganasha },
  { id: 3, title: "Wedding Cards favour box", price: "Rs. 49.45", image: FavourBox },
  { id: 4, title: "Theme Wedding Cards", price: "Rs. 30.00", image: Theme },
  { id: 5, title: "Vintage Wedding Cards", price: "Rs. 30.15", image: Vintage },
  { id: 6, title: "Elegant peacock WeddingCards", price: "Rs. 15.00", image: Peacock },
  { id: 7, title: "Unique Wedding Cards", price: "Rs. 22.50", image: Unique },
  { id: 8, title: "Wardrobe Wedding Cards", price: "Rs. 57.75", image: Wardrobe },
  { id: 9, title: "Foldable Wedding Cards", price: "Rs. 35.55", image: Foldable },
  { id: 10, title: "Traditional Wedding Cards", price: "Rs. 50.00", image: Traditional },
  { id: 11, title: "Royal Scroll Wedding Cards", price: "Rs. 75.00", image: Scroll },
  { id: 12, title: "Gate Fold Wedding Cards", price: "Rs. 43.20", image: Gatefold },
];

const HinduWeddingCards = () => {
  const [wishlist, setWishlist] = useState([]);

  const toggleWishlist = (card) => {
    setWishlist((prev) => {
      const exists = prev.find(item => item.id === card.id);
      const updated = exists
        ? prev.filter(item => item.id !== card.id)
        : [...prev, card];

      // Save to localStorage
      localStorage.setItem('wishlist', JSON.stringify(updated));
      return updated;
    });
  };

  const isWishlisted = (id) => wishlist.some(item => item.id === id);

  return (
    <div className="bg-[#E6E6FA] min-h-screen px-6 md:px-24 py-10 font-[Poppins]">
      <h2 className="text-[24px] md:text-[32px] font-semibold text-center text-gray-800 mb-10">
        HINDU WEDDING CARDS
      </h2>

      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-x-6 gap-y-8">
        {cards.map((card) => (
          <div
            key={card.id}
            className="bg-white relative rounded-md overflow-hidden shadow hover:scale-[1.03] transition-transform duration-300"
          >
            {/* Heart Icon */}
            <div
              className="absolute top-2 right-2 bg-white rounded-full p-2 cursor-pointer shadow"
              onClick={() => toggleWishlist(card)}
            >
              <FaHeart
                className={`text-lg transition-colors ${
                  isWishlisted(card.id) ? 'text-red-500' : 'text-gray-300'
                }`}
              />
            </div>

            <img
              src={card.image}
              alt={card.title}
              className="w-full h-48 object-cover"
            />
            <div className="bg-[#FFE5B4] px-4 py-3">
              <h3 className="text-[16px] text-gray-800 font-medium leading-tight">
                {card.title}
              </h3>
              <p className="text-[#FFAB0D] font-semibold text-[14px] mt-1">
                {card.price}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default HinduWeddingCards;
