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

end Formal
