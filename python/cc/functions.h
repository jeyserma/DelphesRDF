#ifndef FUNCTIONS_LOWPU_H
#define FUNCTIONS_LOWPU_H





float mt_2(float pt1, float phi1, float pt2, float phi2) {
    return std::sqrt(2*pt1*pt2*(1-std::cos(phi1-phi2)));
}

double deltaPhi(float phi1, float phi2) {
    double result = phi1 - phi2;
    while (result > M_PI) result -= 2.0*M_PI;
    while (result <= -1.0*M_PI) result += 2.0*M_PI;
    return result;
}

double deltaR2(float eta1, float phi1, float eta2, float phi2) {
    double deta = eta1-eta2;
    double dphi = deltaPhi(phi1,phi2);
    return deta*deta + dphi*dphi;
}

double recoil(double m_sqrts, ROOT::Math::PtEtaPhiMVector v) {

    ROOT::Math::PtEtaPhiMVector recoil_p4(0, 0, 0, m_sqrts);   
    recoil_p4 -= v;
  
    return recoil_p4.M();
}

double sumScalar(ROOT::VecOps::RVec<double> s) {

    double ret = 0;
	for(unsigned int i = 0; i < s.size(); ++i) ret += s[i];
  
    return ret;
}

ROOT::Math::PtEtaPhiMVector sumP4(ROOT::VecOps::RVec<double> pt, ROOT::VecOps::RVec<double> eta, ROOT::VecOps::RVec<double> phi, ROOT::VecOps::RVec<double> m) {

    ROOT::Math::PtEtaPhiMVector ret(0, 0, 0, 0);
	for(unsigned int i = 0; i < pt.size(); ++i) {
        
        ROOT::Math::PtEtaPhiMVector v(pt[i], eta[i], phi[i], m[i]);
        ret += v;
    }
  
    return ret;
}

ROOT::VecOps::RVec<double> computeEnergy(ROOT::VecOps::RVec<double> pt, ROOT::VecOps::RVec<double> eta, ROOT::VecOps::RVec<double> phi, ROOT::VecOps::RVec<double> m) {

    ROOT::VecOps::RVec<double> ret;
	for(unsigned int i = 0; i < pt.size(); ++i) {
        
        ROOT::Math::PtEtaPhiMVector v(pt[i], eta[i], phi[i], m[i]);
        ret.push_back(v.E());
    }
  
    return ret;
}

#endif