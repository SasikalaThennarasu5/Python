// File: src/components/HowToOrder.jsx
import React from 'react';

const HowToOrder = () => {
  return (
    <div className="bg-[#E6E6FA] px-6 md:px-24 py-10 font-[Poppins] text-[#111827]">
      <h2 className="text-[20px] md:text-[24px] font-semibold mb-6">
        How do I order wedding cards from Wed Knot Craft online?
      </h2>

      <ul className="space-y-4 text-[16px] leading-relaxed">
        <li>
          <span className="font-semibold">Browse the Collection:</span>{' '}
          Take your time to explore our collection and discover various designs that suit your style
          and preferences. You can use the search filters to narrow down your options based on themes,
          colors, or card types.
        </li>
        <li>
          <span className="font-semibold">Select a Design:</span>{' '}
          Once you have found a design that catches your eye, click on it to view more details. You can
          zoom in to see the intricate details and read the card description to ensure it meets your
          requirements.
        </li>
        <li>
          <span className="font-semibold">Add to Cart:</span>{' '}
          Once you are happy with your design, select the quantity and click on the "Add to Cart"
          button to proceed to the next step.
        </li>
        <li>
          <span className="font-semibold">Review Your Order:</span>{' '}
          In the shopping cart, you will be able to review your order summary, including the quantity,
          price, and any additional services you have selected.
        </li>
        <li>
          <span className="font-semibold">Secure Payment:</span>{' '}
          King of Cards offers a secure online payment system. Choose your preferred payment method and
          enter the necessary details to complete your transaction.
        </li>
        <li>
          <span className="font-semibold">Place Your Order:</span>{' '}
          After confirming your payment, you will receive an order confirmation via email, along with
          an estimated delivery date.
        </li>
      </ul>
    </div>
  );
};

export default HowToOrder;
