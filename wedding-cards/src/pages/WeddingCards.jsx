import React from "react";
import { Link } from "react-router-dom";

import hindu1 from "../assets/images/hindu1.png";
import christian2 from "../assets/images/christian2.png";
import muslim2 from "../assets/images/muslim2.png";
import sikh from "../assets/images/sikh.png";
import interfaith1 from "../assets/images/interfaith1.png";
import exclusive from "../assets/images/exclusive.png";
import traditional from "../assets/images/traditional.png";
import all from "../assets/images/all.png";
import newstyle from "../assets/images/newstyle.png";
import envelope from "../assets/images/envelope.png";
import elegant from "../assets/images/elegant.png";
import nepali from "../assets/images/nepali.png";

const weddingCards = [
  { title: "Hindu Wedding Cards", image: hindu1, route: "/HinduWeddingCards" },
  { title: "Christian Wedding Cards", image: christian2, route: "/HinduWeddingCards" },
  { title: "Muslim Wedding Cards", image: muslim2, route: "/HinduWeddingCards" },
  { title: "Sikh Wedding Cards", image: sikh, route: "/HinduWeddingCards" },
  { title: "Interfaith Wedding Cards", image: interfaith1, route: "/HinduWeddingCards" },
  { title: "Exclusive Wedding Cards", image: exclusive, route: "/HinduWeddingCards" },
  { title: "Traditional Wedding Cards", image: traditional, route: "/HinduWeddingCards" },
  { title: "All Wedding Cards", image: all, route: "/HinduWeddingCards" },
  { title: "New Style Wedding Cards", image: newstyle, route: "/HinduWeddingCards" },
  { title: "Envelope Wedding Cards", image: envelope, route: "/HinduWeddingCards" },
  { title: "Elegant Edit Wedding Cards", image: elegant, route: "/HinduWeddingCards" },
  { title: "Nepali Wedding Cards", image: nepali, route: "/HinduWeddingCards" },
];

const WeddingCards = () => {
  return (
    <div className="bg-[#EAE6FA] min-h-screen py-12 px-4 md:px-20 font-poppins">
      <h2 className="text-center text-3xl font-bold text-black mb-12">
        WEDDING CARDS
      </h2>

      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-10 place-items-center">
        {weddingCards.map((card, index) => (
          <Link to={card.route} key={index}>
            <div className="bg-white shadow-lg rounded-xl p-5 w-full max-w-[260px] hover:scale-105 hover:shadow-2xl transition-all duration-300">
              <img
                src={card.image}
                alt={card.title}
                className="w-full h-[280px] object-cover rounded-lg mb-4"
              />
              <p className="text-base text-center font-semibold text-black">
                {card.title}
              </p>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
};

export default WeddingCards;
