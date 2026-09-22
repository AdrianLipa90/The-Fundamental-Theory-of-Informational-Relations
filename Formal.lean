import Std

namespace Formal

/--
A typed affine transition pair. The first component is the linear/frame part;
the second is the translational part.
-/
structure AffinePair (R T : Type) where
  linear : R
  shift : T
deriving Repr

/--
TIR convention for affine SE(3)-style composition:
(R₂,t₂) ∘ (R₁,t₁) = (R₂R₁, R₂·t₁ + t₂).
The operations are kept abstract so this theorem checks the cross-repository
coordinate law without importing any physical interpretation.
-/
def tirCompose {R T : Type}
    (mul : R → R → R)
    (act : R → T → T)
    (add : T → T → T)
    (g₂ g₁ : AffinePair R T) : AffinePair R T :=
  ⟨mul g₂.linear g₁.linear,
   add (act g₂.linear g₁.shift) g₂.shift⟩

/--
RFC GSC4G convention after the explicit symbol map
R_ba ↔ A_qp and t_ba ↔ t_qp.
-/
def rfcCompose {R T : Type}
    (mul : R → R → R)
    (act : R → T → T)
    (add : T → T → T)
    (g₂ g₁ : AffinePair R T) : AffinePair R T :=
  ⟨mul g₂.linear g₁.linear,
   add (act g₂.linear g₁.shift) g₂.shift⟩

/-- FSI.01: the two published coordinate composition laws are identical
under the declared convention map. -/
theorem fsi01_affine_composition_crosswalk
    {R T : Type}
    (mul : R → R → R)
    (act : R → T → T)
    (add : T → T → T)
    (g₂ g₁ : AffinePair R T) :
    tirCompose mul act add g₂ g₁ =
    rfcCompose mul act add g₂ g₁ := by
  rfl

/--
Abstract inverse-coordinate formula shared by the same convention:
(R,t)⁻¹ = (R⁻¹, R⁻¹·(-t)).
-/
def tirInverse {R T : Type}
    (inv : R → R)
    (act : R → T → T)
    (neg : T → T)
    (g : AffinePair R T) : AffinePair R T :=
  ⟨inv g.linear, act (inv g.linear) (neg g.shift)⟩

def rfcInverse {R T : Type}
    (inv : R → R)
    (act : R → T → T)
    (neg : T → T)
    (g : AffinePair R T) : AffinePair R T :=
  ⟨inv g.linear, act (inv g.linear) (neg g.shift)⟩

theorem fsi01_affine_inverse_crosswalk
    {R T : Type}
    (inv : R → R)
    (act : R → T → T)
    (neg : T → T)
    (g : AffinePair R T) :
    tirInverse inv act neg g =
    rfcInverse inv act neg g := by
  rfl



/--
FSI.02 local-to-global cocycle direction. A globally potentialized transition
field has exact identity loops and satisfies the ordered triple-overlap
composition law. The group laws are passed explicitly so the theorem stays
dependency-free and the source repository keeps the interpretation of the
transition algebra.
-/
def transitionFromPotential {G X : Type}
    (mul : G → G → G)
    (inv : G → G)
    (p : X → G) (a b : X) : G :=
  mul (p b) (inv (p a))

theorem transitionFromPotential_refl
    {G X : Type}
    (mul : G → G → G)
    (inv : G → G)
    (one : G)
    (hMulInv : ∀ x : G, mul x (inv x) = one)
    (p : X → G) (a : X) :
    transitionFromPotential mul inv p a a = one := by
  exact hMulInv (p a)

theorem transitionFromPotential_cocycle
    {G X : Type}
    (mul : G → G → G)
    (inv : G → G)
    (one : G)
    (hAssoc : ∀ x y z : G, mul (mul x y) z = mul x (mul y z))
    (hInvMul : ∀ x : G, mul (inv x) x = one)
    (hOneMul : ∀ x : G, mul one x = x)
    (p : X → G) (a b c : X) :
    mul (transitionFromPotential mul inv p b c)
        (transitionFromPotential mul inv p a b) =
      transitionFromPotential mul inv p a c := by
  unfold transitionFromPotential
  rw [hAssoc]
  rw [← hAssoc (inv (p b)) (p b) (inv (p a))]
  rw [hInvMul]
  rw [hOneMul]



/--
FSI.03 TIR-side gauge redundancy: changing the frame at an intermediate
endpoint cancels from a composed transport. Only the endpoint frames remain.
-/
def gaugeEdge {G : Type}
    (mul : G → G → G)
    (inv : G → G)
    (gi gj wij : G) : G :=
  mul (mul gi wij) (inv gj)

theorem gaugeEdge_middle_frame_cancels
    {G : Type}
    (mul : G → G → G)
    (inv : G → G)
    (one : G)
    (hAssoc : ∀ x y z : G, mul (mul x y) z = mul x (mul y z))
    (hInvMul : ∀ x : G, mul (inv x) x = one)
    (hOneMul : ∀ x : G, mul one x = x)
    (gi gj gk wij wjk : G) :
    mul (gaugeEdge mul inv gi gj wij)
        (gaugeEdge mul inv gj gk wjk) =
      gaugeEdge mul inv gi gk (mul wij wjk) := by
  unfold gaugeEdge
  rw [hAssoc]
  rw [← hAssoc (inv gj) (mul gj wjk) (inv gk)]
  rw [← hAssoc (inv gj) gj wjk]
  rw [hInvMul]
  rw [hOneMul]
  rw [← hAssoc (mul gi wij) wjk (inv gk)]
  rw [hAssoc gi wij wjk]

end Formal
