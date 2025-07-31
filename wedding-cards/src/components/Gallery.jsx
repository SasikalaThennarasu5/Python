import React from 'react';
import { Link } from 'react-router-dom';
import hinduImage from '../assets/images/hindu.png';
import christianImage from '../assets/images/christian.jpg';
import muslimImage from '../assets/images/muslim.png';
import interfaithImage from '../assets/images/interfaith.png';

const collections = [
  {
    title: 'Hindu Invitation Collections',
    image: hinduImage,
    path: '/hinduWeddingCards',
  },
  {
    title: 'Christian Invitation Collections',
    image: christianImage,
    path: '/hinduWeddingCards',
  },
  {
    title: 'Muslim Invitation Collections',
    image: muslimImage,
    path: '/hinduWeddingCards',
  },
  {
    title: 'Interfaith Invitation Collections',
    image: interfaithImage,
    path: '/hinduWeddingCards',
  },
];

const Gallery = () => {
  return (
    <div className="bg-[#ebe9fd] py-10 px-6 sm:px-10 md:px-20">
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-10">
        {collections.map((collection, index) => (
          <div
            key={index}
            className="bg-white rounded-md shadow-md overflow-hidden flex flex-col group transform transition duration-500 hover:scale-[1.03] hover:shadow-xl"
          >
            {/* Image Zoom on Hover */}
            <div className="overflow-hidden">
              <img
                src={collection.image}
                alt={collection.title}
                className="w-full h-[400px] object-cover transform transition-transform duration-500 group-hover:scale-110"
              />
            </div>

            <div className="p-4 flex flex-col items-center">
              <h3 className="text-center text-lg font-semibold mb-4">
                {collection.title}
              </h3>

              {collection.path ? (
                <Link to={collection.path}>
                  <button className="bg-orange-600 text-white font-semibold px-6 py-2 rounded-lg shadow-lg hover:bg-orange-700 transition-all duration-300">
  Buy Now
</button>

                </Link>
              ) : (
                <button className="bg-orange-600 text-white font-semibold px-6 py-2 rounded-lg shadow-lg hover:bg-orange-700 transition-all duration-300">
  Buy Now
</button>

              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Gallery;