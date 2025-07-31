import React from "react";
import beachCard from "../assets/images/Hindu_wedding_card.png";
import birdCard from "../assets/images/luxury_card.png";
import palaceCard from "../assets/images/Floral_Indian_wedding_invitation.png";

const cards = [
  {
    title: "Hindu Wedding Cards",
    image: beachCard,
  },
  {
    title: "Luxury Cards",
    image: birdCard,
  },
  {
    title: "Floral Wedding Cards",
    image: palaceCard,
  },
];

const ThemeCards = () => {
  return (
    <section className="bg-[#E6E6FA] py-12 px-6 md:px-24 font-poppins">
      <div className="text-center mb-12">
        <h2 className="text-2xl md:text-3xl font-bold mb-2">Unique and Exclusive Invitation Cards</h2>
        <p className="text-lg">Because Each Wedding is Truly Unique and Memorable</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8 place-items-center">
        {cards.map((card, index) => (
          <div
            key={index}
            className="bg-[#fffde7] shadow-md rounded-md p-4 w-full max-w-xs text-center"
          >
            <div className="w-64 h-64 mx-auto mb-4 overflow-hidden rounded-md">
              <img
                src={card.image}
                alt={card.title}
                className="w-full h-full object-cover transform transition-transform duration-300 hover:scale-110"
              />
            </div>
            <h3 className="text-lg font-semibold">{card.title}</h3>
          </div>
        ))}
      </div>
    </section>
  );
};

export default ThemeCards;
