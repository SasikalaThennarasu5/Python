import React from "react";
import orderSample from "../assets/images/ordersample.png";
import getSample from "../assets/images/getsample.png";
import approveDraft from "../assets/images/approvedraft.png";
import bulkOrder from "../assets/images/bulkorder.png";
import delivery from "../assets/images/delivery.png";

const steps = [
  { title: "Order Sample", icon: orderSample },
  { title: "Get Sample Order In 5 days", icon: getSample },
  { title: "Approve Digital Draft", icon: approveDraft },
  { title: "Place Your Bulk Order", icon: bulkOrder },
  { title: "Print & Delivery", icon: delivery },
];

const HowItWorks = () => {
  return (
    <section className="bg-[#E6E6FA] py-12 px-6 md:px-24 font-poppins">
      <h2 className="text-2xl md:text-3xl font-bold text-center mb-12">
        How It Works
      </h2>

      <div className="grid grid-cols-2 md:grid-cols-5 gap-x-6 gap-y-12 justify-items-center">
        {steps.map((step, index) => (
          <div key={index} className="text-center">
            <img
              src={step.icon}
              alt={step.title}
              className="w-20 h-20 object-contain mx-auto mb-4 transition-transform duration-300 hover:scale-110"
            />
            <p className="text-base font-medium">{step.title}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default HowItWorks;
