import React from 'react';
import { FaStar } from 'react-icons/fa';
import jamesImg from '../assets/images/james.jpg';        // Replace with actual image paths
import harshithaImg from '../assets/images/harshitha.jpg';
import santhoshImg from '../assets/images/santhosh.jpg';

const testimonials = [
  {
    name: 'James',
    title: 'Absolutely beautiful invites!',
    text: 'We were blown away by the quality and elegance of our wedding invitations. The paper felt luxurious, and the printing was flawless. Everyone keeps asking where we got them from!',
    image: jamesImg,
  },
  {
    name: 'Harshitha',
    title: 'Customized to perfection',
    text: 'We wanted something simple but unique, and they absolutely nailed it. Colors, fonts, wording — everything was exactly how we imagined. Fast turnaround too!',
    image: harshithaImg,
  },
  {
    name: 'Santhosh',
    title: 'Great quality at a great price.',
    text: 'We were on a tight budget, but didn’t want to compromise on style. These invites were not only affordable but looked premium. Arrived quickly and packaged beautifully.',
    image: santhoshImg,
  },
];

const Testimonial = () => {
  return (
    <section className="bg-[#E6E6FA] py-16 px-6 md:px-20 font-[Poppins]">
      <h2 className="text-2xl md:text-3xl font-bold text-center mb-12 uppercase">
        What Client Say About Us
      </h2>

      <div className="grid md:grid-cols-3 gap-10">
        {testimonials.map((t, index) => (
          <div
            key={index}
            className="bg-white p-6 rounded-lg shadow-xl hover:shadow-2xl transition duration-300"
          >
            <img
              src={t.image}
              alt={t.name}
              className="w-20 h-20 object-cover rounded-full mx-auto mb-4"
            />
            <h3 className="text-center font-bold text-lg">{t.name}</h3>
            <p className="text-center font-semibold mb-2">{t.title}</p>
            <p className="text-sm text-gray-700 text-center mb-4">{t.text}</p>
            <div className="flex justify-center text-[#FFAB0D] text-xl">
              {[...Array(5)].map((_, i) => (
                <FaStar key={i} />
              ))}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Testimonial;
